'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bernoulli_\ntorch.Tensor.bernoulli_(_input_tensor, p=0.5, *, generator=None)\n'
import torch
import torch
input_tensor = torch.rand(2, 3)
output_tensor = torch.Tensor.bernoulli_(input_tensor, p=0.5)
print('input_tensor:', input_tensor)
print('output_tensor:', output_tensor)
'\nExpected Output:\ninput_tensor: tensor([[0.5193, 0.8983, 0.8180],\n        [0.9061, 0.8381, 0.6930]])\noutput_tensor: tensor([[1., 1., 1.],\n        [1., 1., 0.]])\n'