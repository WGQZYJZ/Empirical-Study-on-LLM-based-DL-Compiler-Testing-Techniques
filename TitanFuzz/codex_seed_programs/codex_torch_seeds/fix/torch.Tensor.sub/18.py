'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sub\ntorch.Tensor.sub(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.rand(5, 3)
other = torch.rand(3)
output_tensor = input_tensor.sub(other)
print('The input tensor is: \n', input_tensor)
print('The other tensor is: \n', other)
print('The output tensor is: \n', output_tensor)