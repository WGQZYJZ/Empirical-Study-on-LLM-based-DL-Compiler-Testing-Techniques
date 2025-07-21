'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.polygamma\ntorch.Tensor.polygamma(_input_tensor, n)\n'
import torch
input_tensor = torch.randn(3, 3)
output_tensor = torch.Tensor.polygamma(input_tensor, 1)
print('Output Tensor: ', output_tensor)