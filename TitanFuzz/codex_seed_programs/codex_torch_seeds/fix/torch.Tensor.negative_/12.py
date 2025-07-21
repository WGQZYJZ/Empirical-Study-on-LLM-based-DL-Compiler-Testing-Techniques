'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.negative_\ntorch.Tensor.negative_(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 4)
print('The input tensor is:', input_tensor)
output_tensor = torch.Tensor.negative_(input_tensor)
print('The output tensor is:', output_tensor)