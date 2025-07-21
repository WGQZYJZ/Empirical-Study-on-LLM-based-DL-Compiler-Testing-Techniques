'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.seed\ntorch.seed()\n'
import torch
import torch
x = torch.randn(100, 1000)
y = torch.randn(1000, 100)
torch.seed()
out = torch.mm(x, y)
print(out)
out = torch.randn(1)
print(out)
torch.cuda.manual_seed_all(0)
torch.cuda.is_available()
torch.cuda.manual_seed(0)