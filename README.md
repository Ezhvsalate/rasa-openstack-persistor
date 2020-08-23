# RASA Openstack persistor

## Purpose
In RASA Open Source [only three options](https://rasa.com/docs/rasa/user-guide/cloud-storage/) for Cloud Storage are available out-of-the-box: AWS S3, GCS and Azure.
This package allows using [Openstack Swift](https://docs.openstack.org/swift/latest/) object storage for that goal.

## Installation
(not released yet)
```
pip install ...
```

## Configuration
The basic way to setup object storage connection is to create [clouds.yaml](https://docs.openstack.org/python-openstackclient/pike/configuration/index.html#configuration-files) file.
OpenStack client will look for configuration file in following places:
* current directory
* ~/.config/openstack
* /etc/openstack

After configuration file is created the only thing you have to specify is environment variable `RASA_OS_CLOUD_NAME`.

## Example

Contents of `clouds.yaml` file:

```yaml
clouds:
  devstack:
    auth:
      auth_url: http://192.168.122.10:35357/
      project_name: demo
      username: demo
      password: 0penstack
    region_name: RegionOne
```
Set a value environment variable:
```bash
RASA_OS_CLOUD_NAME=devstack
RASA_OS_CONTAINER_NAME=anyname
```

Run RASA with `--remote-storage` option:
```bash
  rasa run --remote-storage rasa_openstack_persistor.OpenStackPersistor.OpenStackPersistor
```
