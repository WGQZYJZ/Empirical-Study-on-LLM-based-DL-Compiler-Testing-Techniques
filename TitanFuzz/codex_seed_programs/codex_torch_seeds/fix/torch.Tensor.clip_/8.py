'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.clip_\ntorch.Tensor.clip_(_input_tensor, min=None, max=None)\n'
import torch
input_tensor = torch.randn(4, 5)
output_tensor = input_tensor.clip_((- 0.2), 0.2)
print('input_tensor: {}'.format(input_tensor))
print('output_tensor: {}'.format(output_tensor))