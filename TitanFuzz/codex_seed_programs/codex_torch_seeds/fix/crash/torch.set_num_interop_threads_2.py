'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_num_interop_threads\ntorch.set_num_interop_threads(int)\n'
import torch
input_data = torch.rand(10, 10)
torch.set_num_interop_threads(2)
torch.set_num_threads(4)
print(torch.get_num_interop_threads())
print(torch.get_num_threads())