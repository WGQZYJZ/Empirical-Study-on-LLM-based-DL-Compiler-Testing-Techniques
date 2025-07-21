'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.equal\ntorch.Tensor.equal(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
other = torch.tensor([[1, 2, 3], [4, 5, 6]])
output_tensor = torch.Tensor.equal(input_tensor, other)
print('input_tensor:', input_tensor)
print('other:', other)
print('output_tensor:', output_tensor)