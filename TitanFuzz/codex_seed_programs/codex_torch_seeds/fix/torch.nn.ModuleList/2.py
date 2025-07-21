'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ModuleList\ntorch.nn.ModuleList(modules=None)\n'
import torch
input_data = torch.rand(1, 2, 3, 4)
torch.nn.ModuleList([torch.nn.Linear(3, 4), torch.nn.Linear(3, 4)])