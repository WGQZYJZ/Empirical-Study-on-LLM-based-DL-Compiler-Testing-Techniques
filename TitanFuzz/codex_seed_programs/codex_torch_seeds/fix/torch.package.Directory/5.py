'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.package.Directory\ntorch.package.Directory(name, is_dir)\n'
import torch
import os
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
torch.package.Directory(root_dir, True)