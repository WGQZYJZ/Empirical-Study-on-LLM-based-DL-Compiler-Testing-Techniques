'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.zeros_\ntorch.nn.init.zeros_(tensor)\n'
import torch
input_data = torch.randn(2, 3)
print(input_data)
torch.nn.init.zeros_(input_data)
print(input_data)