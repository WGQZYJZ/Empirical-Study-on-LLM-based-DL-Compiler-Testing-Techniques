'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isreal\ntorch.isreal(input)\n'
import torch
x = torch.tensor([1, 2, 3, 4])
y = torch.tensor([1, 2, 3, 4], dtype=torch.float64)
z = torch.tensor([1, 2, 3, 4], dtype=torch.complex64)
print(torch.isreal(x))
print(torch.isreal(y))
print(torch.isreal(z))