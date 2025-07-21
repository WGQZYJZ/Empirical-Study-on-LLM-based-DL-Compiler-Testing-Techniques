'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.resize_\ntorch.Tensor.resize_(_input_tensor, *sizes, memory_format=torch.contiguous_format)\n'
import torch
input_tensor = torch.randint(low=0, high=10, size=(2, 3, 4))
print('Input tensor: \n', input_tensor)
output_tensor = torch.Tensor.resize_(input_tensor, (2, 3, 5))
print('Output tensor: \n', output_tensor)
'\nTask 4: Call the API torch.Tensor.resize_as_\ntorch.Tensor.resize_as_(_input_tensor, _template_tensor, memory_format=torch.contiguous_format)\n'
output_tensor = torch.Tensor.resize_as_(input_tensor, torch.randint(low=0, high=10, size=(2, 3, 5)))
print('Output tensor: \n', output_tensor)