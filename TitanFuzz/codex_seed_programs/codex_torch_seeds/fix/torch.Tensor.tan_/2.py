'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tan_\ntorch.Tensor.tan_(_input_tensor)\n'
import torch
input_tensor = torch.rand(2, 3)
output_tensor = torch.Tensor.tan_(input_tensor)
print('The input tensor: ', input_tensor)
print('The output tensor: ', output_tensor)