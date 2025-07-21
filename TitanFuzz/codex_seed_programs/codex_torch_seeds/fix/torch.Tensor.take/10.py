'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.take\ntorch.Tensor.take(_input_tensor, indices)\n'
import torch
input_tensor = torch.rand(10, 10)
indices = torch.tensor([0, 1, 2, 3, 4])
print('Input tensor: ', input_tensor)
print('Indices: ', indices)
result = torch.Tensor.take(input_tensor, indices)
print('Result: ', result)