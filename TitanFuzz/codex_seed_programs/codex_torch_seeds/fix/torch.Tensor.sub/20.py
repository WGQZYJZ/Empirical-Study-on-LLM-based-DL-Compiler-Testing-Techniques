'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sub\ntorch.Tensor.sub(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.rand(10, 20)
other = torch.rand(10, 20)
output_tensor = input_tensor.sub(other)
print('The input tensor is: {}'.format(input_tensor))
print('The other tensor is: {}'.format(other))
print('The output tensor is: {}'.format(output_tensor))