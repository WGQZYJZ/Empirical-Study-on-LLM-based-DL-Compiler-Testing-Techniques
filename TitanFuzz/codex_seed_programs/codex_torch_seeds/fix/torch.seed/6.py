'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.seed\ntorch.seed()\n'
import torch
x = torch.randn(2, 3)
print(x)
torch.seed()
print(torch.randn(2, 3))
print(torch.randn(2, 3))
torch.cuda.manual_seed(1)
print(torch.randn(2, 3))
torch.cuda.manual_seed_all(1)
print(torch.randn(2, 3))