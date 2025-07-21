'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_num_threads\ntorch.set_num_threads(int)\n'
import torch
x = torch.rand(5, 3)
y = torch.rand(5, 3)
torch.set_num_threads(2)
z = torch.add(x, y)
print(z)
print(torch.get_num_threads())