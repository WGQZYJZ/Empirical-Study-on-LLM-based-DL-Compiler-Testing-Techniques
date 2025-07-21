'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arccos\ntorch.Tensor.arccos(_input_tensor)\n'
import torch
x = torch.Tensor([1, 2, 3, 4, 5])
y = torch.Tensor([6, 7, 8, 9, 10])
print(torch.arccos(x))
print(torch.arccos(y))
x = torch.Tensor([1, 2, 3, 4, 5])
y = torch.Tensor([6, 7, 8, 9, 10])
print(x.arccos())
print(y.arccos())