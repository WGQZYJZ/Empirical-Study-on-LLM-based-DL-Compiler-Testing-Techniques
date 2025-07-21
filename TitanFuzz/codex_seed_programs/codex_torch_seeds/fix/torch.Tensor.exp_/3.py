'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.exp_\ntorch.Tensor.exp_(_input_tensor)\n'
import torch
input_tensor = torch.arange(1, 11, dtype=torch.float32).reshape(2, 5)
output_tensor = torch.Tensor.exp_(input_tensor)
print('input_tensor: ', input_tensor)
print('output_tensor: ', output_tensor)