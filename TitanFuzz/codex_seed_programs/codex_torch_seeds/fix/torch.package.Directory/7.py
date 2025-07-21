'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.package.Directory\ntorch.package.Directory(name, is_dir)\n'
import torch
input_data = torch.randn(1, 2)
print('Input data: ', input_data)
torch.package.Directory(input_data, True)