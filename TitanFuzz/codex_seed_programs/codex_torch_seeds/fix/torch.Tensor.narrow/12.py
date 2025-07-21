'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.narrow\ntorch.Tensor.narrow(_input_tensor, dimension, start, length)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print(input_tensor)
print(torch.Tensor.narrow(input_tensor, 0, 0, 2))
print(torch.Tensor.narrow(input_tensor, 1, 0, 3))
print(torch.Tensor.narrow(input_tensor, 1, 1, 2))
print(torch.Tensor.narrow(input_tensor, 0, 1, 2))
print(torch.Tensor.narrow(input_tensor, 0, 0, 1))
print(torch.Tensor.narrow(input_tensor, 0, 1, 1))
print(torch.Tensor.narrow(input_tensor, 0, 2, 1))