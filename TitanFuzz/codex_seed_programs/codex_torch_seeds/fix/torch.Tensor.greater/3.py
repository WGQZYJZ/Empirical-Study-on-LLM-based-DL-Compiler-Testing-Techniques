'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.greater\ntorch.Tensor.greater(_input_tensor, other)\n'
import torch
import torch
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
output_tensor = torch.Tensor.greater(input_tensor, 5)
print('input_tensor:', input_tensor)
print('output_tensor:', output_tensor)
'\ninput_tensor: tensor([[1., 2., 3.],\n        [4., 5., 6.],\n        [7., 8., 9.]])\noutput_tensor: tensor([[False, False, False],\n        [False, False,  True],\n        [ True,  True,  True]], dtype=torch.uint8)\n'