'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.frac_\ntorch.Tensor.frac_(_input_tensor)\n'
import torch
input_tensor = torch.rand(4, 4)
print('Input tensor: ', input_tensor)
frac_result = torch.Tensor.frac_(input_tensor)
print('Result of torch.Tensor.frac_: ', frac_result)