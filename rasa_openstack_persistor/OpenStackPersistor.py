import openstack
import os
from rasa.nlu.persistor import Persistor
import logging
from typing import Text, List

logger = logging.getLogger(__name__)


class OpenStackPersistor(Persistor):
    def __init__(self):
        self.container_name = os.environ.get('RASA_OS_CONTAINER_NAME')
        cloud_name = os.environ.get('RASA_OS_CLOUD_NAME')
        self.os = openstack.connect(cloud=cloud_name)
        self.container = self.os.create_container(name=self.container_name, public=False)

    def list_models(self) -> List[Text]:
        try:
            return [self._model_dir_and_model_from_filename(obj)[1] for obj in self.os.list_objects(self.container)]
        except Exception as e:
            logger.warning(f"Failed to list models in OpenStack Swift. {e}")
            return []

    def _persist_tar(self, filekey: Text, tar_path: Text) -> None:
        self.os.create_object(self.container_name, filekey, tar_path)

    def _retrieve_tar(self, model_path: Text) -> None:
        tar_name = os.path.basename(model_path)
        self.os.get_object(self.container_name, model_path, outfile=tar_name)
