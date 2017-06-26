#
# Copyright (c) 2017 nexB Inc. and others. All rights reserved.
# http://nexb.com and https://github.com/nexB/scancode-toolkit/
# The ScanCode software is licensed under the Apache License version 2.0.
# Data generated with ScanCode require an acknowledgment.
# ScanCode is a trademark of nexB Inc.
#
# You may not use this software except in compliance with the License.
# You may obtain a copy of the License at: http://apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
#
# When you publish or redistribute any data created with ScanCode or any ScanCode
# derivative work, you must accompany this data with the following acknowledgment:
#
#  Generated with ScanCode and provided on an "AS IS" BASIS, WITHOUT WARRANTIES
#  OR CONDITIONS OF ANY KIND, either express or implied. No content created from
#  ScanCode should be considered or used as legal advice. Consult an Attorney
#  for any legal advice.
#  ScanCode is a free software code scanning tool from nexB Inc. and others.
#  Visit https://github.com/nexB/scancode-toolkit/ for support and download.

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import os

import pluggy
import click


hookimpl = pluggy.HookimplMarker('scan_proper')

formats = ['json', 'json-pp', 'html', 'html-app', 'spdx-tv', 'spdx-rdf']
plugin_formats = {}

@hookimpl
def add_cmdline_option(post_scan_plugins):
    """
    Add --format option to scancode
    """
    plugins = post_scan_plugins.hook.add_format()
    for format, plugin in plugins:
            if (plugin not in plugin_formats):
                plugin_formats[format] = plugin

    option = click.Option(('-f', '--format',), is_flag=False, default='json', show_default=True, metavar='<style>',
              help=('Set <output_file> format <style> to one of the standard formats: %s '
                    'or the path to a custom template' % ' or '.join(formats + plugin_formats.keys())),
              callback=validate_formats)
    return option

def validate_formats(ctx, param, value):
    """
    Validate formats and template files. Raise a BadParameter on errors.
    """
    if check_if_template(value):
        return value
    else:
        return value.lower()

def check_if_template(format):
    format_lower = format.lower()
    if format_lower in plugin_formats or format_lower in formats:
        return False
    # render using a user-provided custom format template
    if not os.path.isfile(format):
        raise click.BadParameter('Invalid template file: "%(format)s" does not exist or is not readable.' % locals())
    return True
