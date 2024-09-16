# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from ansible.module_utils.basic import AnsibleModule, sanitize_keys
from ansible.module_utils.basic import missing_required_lib

try:
    import openstack

    HAS_OPENSTACK = True
except ImportError:
    HAS_OPENSTACK = False


class ApplicationCredentialsModule:
    argument_spec = dict(
        cloud=dict(type="raw", no_log=True),
        name=dict(type="str"),
        unrestricted=dict(type="bool", default=False),
        state=dict(
            type="str", default="present", chocies=["present", "absent"]
        ),
    )
    module_kwargs = {
        "supports_check_mode": True,
    }

    def __init__(self):

        self.ansible = AnsibleModule(self.argument_spec, **self.module_kwargs)
        self.params = self.ansible.params
        self.module_name = self.ansible._name
        self.exit_json = self.ansible.exit_json
        self.fail_json = self.ansible.fail_json
        self.vault_addr = None
        self.token = None

    def __call__(self):
        if not HAS_OPENSTACK:
            self.fail_json(msg=missing_required_lib("openstacksdk"))

        try:
            conn = openstack.connect(**self.params["cloud"])
            user_id = conn.session.get_user_id()
            app_cred = conn.identity.find_application_credential(
                user=user_id,
                name_or_id=self.params["name"],
                ignore_missing=True,
            )
            if self.params["state"] == "present":
                if not app_cred:
                    app_cred = conn.identity.create_application_credential(
                        user=user_id,
                        name=self.params["name"],
                        unrestricted=self.params["unrestricted"],
                    )
                self.exit_json(
                    changed=False,
                    application_credential=sanitize_keys(
                        app_cred, self.ansible.no_log_values, []
                    ),
                )
            elif self.params["state"] == "absent" and app_cred:
                conn.identity.delete_application_credential(
                    user=user_id, application_credential=app_cred
                )
                self.exit_json(changed=True)

        except openstack.exceptions.SDKException as e:
            self.fail_json(msg="Failure connecting to the cloud", error=str(e))

        except Exception as ex:
            self.fail_json(
                msg="Exception during application credentials processing",
                error=str(ex),
            )


def main():
    module = ApplicationCredentialsModule()
    module()


if __name__ == "__main__":
    main()
