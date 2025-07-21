'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bernoulli_\ntorch.Tensor.bernoulli_(_input_tensor, p=0.5, *, generator=None)\n'
import torch
input_data = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
output_data = torch.Tensor.bernoulli_(input_data, p=0.5)
print('input_data:', input_data)
print('output_data:', output_data)