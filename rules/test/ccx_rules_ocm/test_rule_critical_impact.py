# Copyright 2020 Red Hat, Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This rule will always fire on all reports. It doesn't like them.
"""
from insights.core.plugins import make_fail
from insights.core.plugins import rule


ERROR_KEY = "TEST_CRITICAL_IMPACT_ERROR"


@rule()
def report():
    return make_fail(ERROR_KEY)
