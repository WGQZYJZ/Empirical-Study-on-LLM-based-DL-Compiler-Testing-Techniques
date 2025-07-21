'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sigmoid\ntorch.Tensor.sigmoid(_input_tensor)\n'
import torch
input_tensor = torch.tensor([[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]])
output_tensor = torch.Tensor.sigmoid(input_tensor)
print('input_tensor:', input_tensor)
print('output_tensor:', output_tensor)
'\nExpected output:\ninput_tensor: tensor([[0., 0.],\n        [0., 1.],\n        [1., 0.],\n        [1., 1.]])\noutput_tensor: tensor([[0.5000, 0.5000],\n        [0.5000, 0.7311],\n        [0.7311, 0.5000],\n        [0.7311, 0.7311]])\n'