'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.get_num_threads\ntorch.get_num_threads()\n'
import torch
x = torch.rand(1000, 1000)
y = torch.rand(1000, 1000)
print('torch.get_num_threads() = {}'.format(torch.get_num_threads()))
torch.set_num_threads(2)
print('torch.get_num_threads() = {}'.format(torch.get_num_threads()))
print('torch.get_num_interop_threads() = {}'.format(torch.get_num_interop_threads()))
torch.set_num_interop_threads(2)