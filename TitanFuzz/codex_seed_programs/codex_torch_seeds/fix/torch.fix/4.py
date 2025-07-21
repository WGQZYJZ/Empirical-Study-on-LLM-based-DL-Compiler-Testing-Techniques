'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fix\ntorch.fix(input, *, out=None)\n'
import torch
torch.__version__
x = torch.randn(4, 4)
print(x)
torch.fix(x)