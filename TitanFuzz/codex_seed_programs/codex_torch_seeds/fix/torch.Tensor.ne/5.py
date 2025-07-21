'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ne\ntorch.Tensor.ne(_input_tensor, other)\n'
import torch
input_tensor = torch.randn(4, 4)
output_tensor = torch.Tensor.ne(input_tensor, input_tensor)
print('Output tensor: ', output_tensor)