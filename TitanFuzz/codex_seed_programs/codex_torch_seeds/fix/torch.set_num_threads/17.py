'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_num_threads\ntorch.set_num_threads(int)\n'
import torch
x = torch.rand(10)
print('x = ', x)
torch.set_num_threads(2)
print('torch.get_num_threads() = ', torch.get_num_threads())