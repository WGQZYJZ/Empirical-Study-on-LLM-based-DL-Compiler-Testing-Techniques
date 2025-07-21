'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.xavier_uniform_\ntorch.nn.init.xavier_uniform_(tensor, gain=1.0)\n'
import torch
import torch
tensor = torch.empty(3, 3)
torch.nn.init.xavier_uniform_(tensor, gain=1.0)
print(tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.xavier_normal_\ntorch.nn.init.xavier_normal_(tensor, gain=1.0)\n'
import torch
import torch
tensor = torch.empty(3, 3)
torch.nn.init.xavier_normal_(tensor, gain=1.0)
print(tensor)