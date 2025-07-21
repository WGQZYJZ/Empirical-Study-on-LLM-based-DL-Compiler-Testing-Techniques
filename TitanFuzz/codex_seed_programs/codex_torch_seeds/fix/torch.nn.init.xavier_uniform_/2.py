'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.xavier_uniform_\ntorch.nn.init.xavier_uniform_(tensor, gain=1.0)\n'
import torch
import torch
input_tensor = torch.rand(3, 5)
torch.nn.init.xavier_uniform_(input_tensor)
print(input_tensor)