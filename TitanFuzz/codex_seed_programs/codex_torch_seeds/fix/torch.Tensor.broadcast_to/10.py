'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.broadcast_to\ntorch.Tensor.broadcast_to(_input_tensor, shape)\n'
import torch
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
print('input tensor:', input_tensor)
output_tensor = torch.Tensor.broadcast_to(input_tensor, (2, 3, 3))
print('output tensor:', output_tensor)
'\nExpected output:\ninput tensor: tensor([[1, 2, 3],\n        [4, 5, 6]])\noutput tensor: tensor([[[1, 2, 3],\n         [1, 2, 3],\n         [1, 2, 3]],\n        [[4, 5, 6],\n         [4, 5, 6],\n         [4, 5, 6]]])\n'