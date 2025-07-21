'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.get_num_threads\ntorch.get_num_threads()\n'
import torch
x = torch.rand(100, 100)
y = torch.rand(100, 100)
torch.get_num_threads()
torch.set_num_threads(4)
torch.get_num_threads()
torch.set_num_threads(8)
torch.get_num_threads()
torch.get_num_interop_threads()
torch.set_num_interop_threads(4)