'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.repeat\ntorch.Tensor.repeat(_input_tensor, *sizes)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(input_tensor.repeat(2, 2))
print(input_tensor.repeat(2, 2, 1))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.reshape\ntorch.Tensor.reshape(_input_tensor, *shape)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(input_tensor.reshape(3, 2))
print(input_tensor.reshape(6, 1))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.squeeze\ntorch.Tensor.squeeze(_input_tensor, *dim)\n'
import torch