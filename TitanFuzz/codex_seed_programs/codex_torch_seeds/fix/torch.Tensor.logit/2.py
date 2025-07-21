'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logit\ntorch.Tensor.logit(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3, 4)
output_tensor = torch.Tensor.logit(input_tensor)
print('input tensor:', input_tensor)
print('output tensor:', output_tensor)