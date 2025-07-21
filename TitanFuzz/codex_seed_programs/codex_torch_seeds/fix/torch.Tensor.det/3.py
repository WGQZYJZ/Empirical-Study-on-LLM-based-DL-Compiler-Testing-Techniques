'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.det\ntorch.Tensor.det(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3, 3)
output_tensor = torch.Tensor.det(input_tensor)
print('The input tensor is:', input_tensor)
print('The output tensor is:', output_tensor)