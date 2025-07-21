'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.zeros_\ntorch.nn.init.zeros_(tensor)\n'
import torch
input_tensor = torch.randn(5, 3)
print(input_tensor)
torch.nn.init.zeros_(input_tensor)
print(input_tensor)