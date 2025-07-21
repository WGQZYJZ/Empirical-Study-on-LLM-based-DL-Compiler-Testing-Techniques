'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.any\ntorch.Tensor.any(_input_tensor, dim=None, keepdim=False)\n'
import torch
_input_tensor = torch.randint(0, 10, (3, 3))
print('Input tensor: {}'.format(_input_tensor))
_any_tensor = torch.Tensor.any(_input_tensor, dim=None, keepdim=False)
print('Any tensor: {}'.format(_any_tensor))
'\nOutput:\n    Input tensor: tensor([[8, 3, 7],\n            [7, 9, 5],\n            [3, 2, 5]])\n    Any tensor: tensor(True)\n'