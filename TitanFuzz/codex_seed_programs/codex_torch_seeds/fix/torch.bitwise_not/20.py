'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_not\ntorch.bitwise_not(input, *, out=None)\n'
import torch
input_tensor = torch.tensor([True, False, True, False], dtype=torch.bool)
print('Input Tensor: ', input_tensor)
output_tensor = torch.bitwise_not(input_tensor)
print('Output Tensor: ', output_tensor)