'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.gcd_\ntorch.Tensor.gcd_(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([15, 21, 35, 105], dtype=torch.int32)
print('Input tensor: ', input_tensor)
print('Output tensor: ', input_tensor.gcd_(7))