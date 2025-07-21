'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.msort\ntorch.Tensor.msort(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 5)
print('Input tensor: \n', input_tensor)
output_tensor = torch.Tensor.msort(input_tensor)
print('Output tensor: \n', output_tensor)