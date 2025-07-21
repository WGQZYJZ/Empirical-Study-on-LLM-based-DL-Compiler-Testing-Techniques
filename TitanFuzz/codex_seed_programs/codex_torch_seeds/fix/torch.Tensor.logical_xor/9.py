'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logical_xor\ntorch.Tensor.logical_xor(_input_tensor, other)\n'
import torch
input_tensor = torch.Tensor([[True, True], [True, False], [False, True], [False, False]])
other = torch.Tensor([[True, True], [True, False], [False, True], [False, False]])
output_tensor = torch.Tensor.logical_xor(input_tensor, other)
print('The input tensor is: {}'.format(input_tensor))
print('The output tensor is: {}'.format(output_tensor))