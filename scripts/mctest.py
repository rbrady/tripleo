# License for the specific language governing permissions and limitations
# under the License.
# !/usr/bin/env python
import logging
import os
import pdb
from mistralclient.api import client as mistral_client

from pprint import pprint

LOG = logging.getLogger(__name__)


def test_mistral():

    wc = mistral_client.client(
        auth_token=os.environ.get('KEYSTONE_AUTH_TOKEN'),
        mistral_url="http://192.0.2.1:8989/v2 "
    )
    pdb.set_trace()
    wf_env = wc.environments.get('overcloud')

    processed_data = dict()
    processed_data['files'] = dict()

    # if there are parameter values input from a user and stored
    # in the mistral environment, add them to the files dict sent
    # to heat and identify them in 'environment_files'.  The create_stack
    # method in the heat client takes care of merging this environment
    # data on the server.
    parameter_defaults = wf_env.variables.get('parameter_defaults')
    if parameter_defaults:
        processed_data['files']['user_set_params'] = parameter_defaults
        processed_data['environment_files'] = ['user_set_params']
    pdb.set_trace()


if __name__ == "__main__":
    test_mistral()

