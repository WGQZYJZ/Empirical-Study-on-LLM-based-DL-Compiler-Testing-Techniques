'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.constant_\ntorch.nn.init.constant_(tensor, val)\n'
import torch
import torch
input_data = torch.randn(5, 5)
torch.nn.init.constant_(input_data, val=0.0)
print(input_data)