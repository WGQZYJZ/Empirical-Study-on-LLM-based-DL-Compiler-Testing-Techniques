'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_floating_point\ntorch.Tensor.is_floating_point(_input_tensor)\n'
import torch
input_tensor = torch.rand(1, 3, 224, 224)
output_tensor = torch.Tensor.is_floating_point(input_tensor)
print('Is the input tensor floating point? ', output_tensor)