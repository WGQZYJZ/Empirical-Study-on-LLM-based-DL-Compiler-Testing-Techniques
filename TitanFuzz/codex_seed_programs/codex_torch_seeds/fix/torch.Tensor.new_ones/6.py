'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_ones\ntorch.Tensor.new_ones(_input_tensor, size, dtype=None, device=None, requires_grad=False)\n'
import torch
_input_tensor = torch.randn(2, 3)
print('Input tensor: {}'.format(_input_tensor))
_output_tensor = torch.Tensor.new_ones(_input_tensor, (2, 3))
print('Output tensor: {}'.format(_output_tensor))
'\nOutput:\nInput tensor: tensor([[-0.7232, -0.6154, -0.8183],\n        [ 0.5235,  0.0337,  0.7992]])\nOutput tensor: tensor([[1., 1., 1.],\n        [1., 1., 1.]])\n'