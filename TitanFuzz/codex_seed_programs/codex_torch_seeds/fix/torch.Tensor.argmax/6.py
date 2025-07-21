'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.argmax\ntorch.Tensor.argmax(_input_tensor, dim=None, keepdim=False)\n'
import torch
_input_tensor = torch.rand(2, 3)
print('Input data: {}'.format(_input_tensor))
print('Argmax result: {}'.format(_input_tensor.argmax(dim=1)))