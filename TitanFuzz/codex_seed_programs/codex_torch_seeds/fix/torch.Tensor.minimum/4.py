'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.minimum\ntorch.Tensor.minimum(_input_tensor, other)\n'
import torch
input_tensor = torch.rand(2, 2)
other_tensor = torch.rand(2, 2)
output_tensor = input_tensor.minimum(other_tensor)
print('Input tensor is:', input_tensor)
print('Other tensor is:', other_tensor)
print('Output tensor is:', output_tensor)