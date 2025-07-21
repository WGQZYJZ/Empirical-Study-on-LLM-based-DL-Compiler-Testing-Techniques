'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.div\ntorch.Tensor.div(_input_tensor, value, *, rounding_mode=None)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
print('\n Input tensor: ', input_tensor)
output_tensor = torch.Tensor.div(input_tensor, 2)
print('\n Output tensor: ', output_tensor)