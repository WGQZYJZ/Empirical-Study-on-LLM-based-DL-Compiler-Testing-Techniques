'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tan\ntorch.Tensor.tan(_input_tensor)\n'
import torch
_input_tensor = torch.randn(5, 3)
output_tensor = torch.Tensor.tan(_input_tensor)
print('output_tensor: ', output_tensor)