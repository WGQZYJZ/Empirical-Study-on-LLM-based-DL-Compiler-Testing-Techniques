'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.orthogonal_\ntorch.nn.init.orthogonal_(tensor, gain=1)\n'
import torch
import torch
input_tensor = torch.randn(2, 3)
print(input_tensor)
torch.nn.init.orthogonal_(input_tensor)
print(input_tensor)