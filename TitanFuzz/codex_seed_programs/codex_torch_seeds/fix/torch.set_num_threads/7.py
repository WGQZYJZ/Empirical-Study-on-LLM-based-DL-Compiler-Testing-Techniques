'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_num_threads\ntorch.set_num_threads(int)\n'
import torch
x = torch.randn(5, 5)
print(x)
torch.set_num_threads(8)