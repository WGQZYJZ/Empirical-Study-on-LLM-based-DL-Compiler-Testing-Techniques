'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.igammac\ntorch.Tensor.igammac(_input_tensor, other)\n'
import torch
print('========== Task 1 ==========')
print('PyTorch version: {}'.format(torch.__version__))
print('========== Task 2 ==========')
input_tensor = torch.randn(2, 3)
other = torch.randn(2, 3)
print('Input tensor: {}'.format(input_tensor))
print('Other tensor: {}'.format(other))
print('========== Task 3 ==========')
print('Calling igammac API: {}'.format(torch.Tensor.igammac(input_tensor, other)))