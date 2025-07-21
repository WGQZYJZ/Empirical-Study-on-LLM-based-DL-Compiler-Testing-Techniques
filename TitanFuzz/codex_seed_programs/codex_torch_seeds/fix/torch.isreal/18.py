'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isreal\ntorch.isreal(input)\n'
import torch
x = torch.randn(1)
print(x)
print(x.item())
print(torch.isreal(x))
print(torch.isreal((x + 1j)))
print(torch.isreal(torch.tensor([2.2])))