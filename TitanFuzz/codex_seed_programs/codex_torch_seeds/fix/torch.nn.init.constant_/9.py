'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.constant_\ntorch.nn.init.constant_(tensor, val)\n'
import torch
input_data = torch.randn(2, 2)
torch.nn.init.constant_(input_data, 0)
print(input_data)