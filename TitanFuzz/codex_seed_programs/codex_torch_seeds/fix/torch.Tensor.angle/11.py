'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.angle\ntorch.Tensor.angle(_input_tensor)\n'
import torch
_input_tensor = torch.randn(1, 2, 3, 4, 5)
output_tensor = torch.Tensor.angle(_input_tensor)
print('output_tensor = ', output_tensor)