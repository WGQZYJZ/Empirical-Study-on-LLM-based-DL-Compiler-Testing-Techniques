'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_num_interop_threads\ntorch.set_num_interop_threads(int)\n'
import torch
input = torch.randn(1, 2)
print(input)
torch.set_num_interop_threads(2)