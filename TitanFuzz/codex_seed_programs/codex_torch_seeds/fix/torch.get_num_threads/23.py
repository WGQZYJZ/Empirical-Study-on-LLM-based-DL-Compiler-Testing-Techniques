'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.get_num_threads\ntorch.get_num_threads()\n'
import torch
x = torch.rand(1000000, 100)
y = torch.rand(1000000, 100)
print(torch.get_num_threads())