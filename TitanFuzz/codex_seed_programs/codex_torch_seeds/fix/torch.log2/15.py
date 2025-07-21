'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.log2\ntorch.log2(input, *, out=None)\n'
import torch
input_tensor = torch.randint(10, (2, 3), dtype=torch.float)
print('Input Tensor: ', input_tensor)
output_tensor = torch.log2(input_tensor)
print('Output Tensor: ', output_tensor)