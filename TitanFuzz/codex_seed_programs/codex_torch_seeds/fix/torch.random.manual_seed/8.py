'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.random.manual_seed\ntorch.random.manual_seed(seed)\n'
import torch
import torch
x = torch.rand(10)
torch.random.manual_seed(5)
print(x)
print(torch.rand(10))
torch.random.manual_seed(5)
print(torch.rand(10))
print(torch.rand(10))
print(torch.rand(10))
print(torch.rand(10))