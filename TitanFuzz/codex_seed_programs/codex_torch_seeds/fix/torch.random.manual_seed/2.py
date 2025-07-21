'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.random.manual_seed\ntorch.random.manual_seed(seed)\n'
import torch
data = torch.randn(2, 3)
print(data)
torch.random.manual_seed(7)
print(torch.rand(2, 3))
torch.random.manual_seed(7)
print(torch.rand(2, 3))
torch.random.manual_seed(7)
print(torch.rand(4, 3))