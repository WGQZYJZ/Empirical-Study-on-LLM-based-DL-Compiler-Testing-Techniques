'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.random.manual_seed\ntorch.random.manual_seed(seed)\n'
import torch
x = torch.rand(5, 3)
print(x)
torch.random.manual_seed(1)
y = torch.rand(5, 3)
print(y)
torch.random.manual_seed(1)
z = torch.rand(5, 3)
print(z)
torch.random.manual_seed(2)
a = torch.rand(5, 3)
print(a)