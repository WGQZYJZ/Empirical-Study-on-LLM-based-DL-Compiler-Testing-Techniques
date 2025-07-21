'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.normal_\ntorch.Tensor.normal_(_input_tensor, mean=0, std=1, *, generator=None)\n'
import torch
input_tensor = torch.randint(10, (2, 3), dtype=torch.float)
print('Input tensor: ', input_tensor)
output_tensor = torch.Tensor.normal_(input_tensor, mean=1, std=3)
print('Output tensor: ', output_tensor)