'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.addcdiv\ntorch.addcdiv(input, tensor1, tensor2, *, value=1, out=None)\n'
import torch
import torch
x = torch.randn(4, 4)
y = torch.randn(4, 4)
z = torch.randn(4, 4, requires_grad=True)
torch.addcdiv(x, y, z, value=0.1)