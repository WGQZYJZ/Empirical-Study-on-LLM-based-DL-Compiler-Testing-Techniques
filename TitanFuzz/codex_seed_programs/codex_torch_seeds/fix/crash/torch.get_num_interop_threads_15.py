'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.get_num_interop_threads\ntorch.get_num_interop_threads()\n'
import torch
import torch
a = torch.rand(1000, 1000)
b = torch.rand(1000, 1000)
torch.get_num_interop_threads()
torch.set_num_interop_threads(4)
torch.get_num_interop_threads()
torch.set_num_interop_threads(8)
torch.get_num_interop_threads()