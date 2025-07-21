'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.all\ntorch.all(input, dim, keepdim=False, *, out=None)\n'
import torch
input_data = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(input_data)
print(torch.all((input_data > 0)))
print(torch.all((input_data > 0), dim=0))
print(torch.all((input_data > 0), dim=1))
print(torch.all((input_data > 0), dim=1, keepdim=True))