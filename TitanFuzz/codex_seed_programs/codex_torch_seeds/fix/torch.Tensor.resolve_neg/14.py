'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.resolve_neg\ntorch.Tensor.resolve_neg(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 3)
print('Input tensor: \n', input_tensor)
output_tensor = torch.Tensor.resolve_neg(input_tensor)
print('Output tensor: \n', output_tensor)