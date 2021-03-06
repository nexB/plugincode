#
# Copyright (c) nexB Inc. and others.
# SPDX-License-Identifier: Apache-2.0
#
# Visit https://aboutcode.org and https://github.com/nexB/ for support and download.
# ScanCode is a trademark of nexB Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from plugincode import CodebasePlugin
from plugincode import PluginManager
from plugincode import HookimplMarker
from plugincode import HookspecMarker

stage = 'post_scan'
entrypoint = 'scancode_post_scan'

post_scan_spec = HookspecMarker(project_name=stage)
post_scan_impl = HookimplMarker(project_name=stage)


@post_scan_spec
class PostScanPlugin(CodebasePlugin):
    """
    A post-scan plugin base class that all post-scan plugins must extend.
    """
    pass


post_scan_plugins = PluginManager(
    stage=stage,
    module_qname=__name__,
    entrypoint=entrypoint,
    plugin_base_class=PostScanPlugin
)
