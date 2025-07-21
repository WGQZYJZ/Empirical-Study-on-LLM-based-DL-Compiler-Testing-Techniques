'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ndimension\ntorch.Tensor.ndimension(_input_tensor)\n'
import torch
_input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(_input_tensor.ndimension())
print(_input_tensor.size())
print(_input_tensor.shape)
print(_input_tensor.numel())
print(_input_tensor.dim())
print(_input_tensor.reshape(3, 2))
print(_input_tensor.view(3, 2))
print(_input_tensor.squeeze())