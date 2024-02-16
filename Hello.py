# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
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

import streamlit as st
import subprocess
import os

# Function to run cookiecutter
def run_cookiecutter(template_path, extra_args):
    command = ["cookiecutter", template_path] + extra_args
    subprocess.run(command, check=True)

# Streamlit UI
st.title("Project Initialization")

# Collect inputs
project_name = st.text_input("Project Name")
other_parameter = st.text_input("Other Parameter")

if st.button("Create Project"):
    if project_name:
        # Assuming you want to pass these as arguments to cookiecutter
        args = ['--no-input', f'project_name={project_name}', f'other_parameter={other_parameter}']
        run_cookiecutter('/path/to/cookiecutter-template', args)
        st.success("Project Created")
    else:
        st.error("Please enter a project name")

if __name__ == "__main__":
    run()
