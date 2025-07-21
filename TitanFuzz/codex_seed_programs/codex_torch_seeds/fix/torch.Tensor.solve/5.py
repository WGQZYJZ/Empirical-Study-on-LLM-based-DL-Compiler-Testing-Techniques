'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.solve\ntorch.Tensor.solve(_input_tensor, A)\n'
import torch
from torch.autograd import Variable
A = torch.Tensor([[1, 2], [3, 4]])
b = torch.Tensor([[5], [6]])
x = torch.Tensor.solve(b, A)
print(x)