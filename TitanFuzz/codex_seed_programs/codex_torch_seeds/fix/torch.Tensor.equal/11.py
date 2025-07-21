'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.equal\ntorch.Tensor.equal(_input_tensor, other)\n'
import torch
input_tensor = torch.rand(2, 5)
other = torch.rand(2, 5)
result = input_tensor.equal(other)
print('input_tensor:', input_tensor)
print('other:', other)
print('result:', result)