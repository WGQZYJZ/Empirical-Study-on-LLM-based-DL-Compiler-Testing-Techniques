'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.resolve_neg\ntorch.Tensor.resolve_neg(_input_tensor)\n'
import torch
input_tensor = torch.rand(2, 3)
print('Input tensor: ', input_tensor)
resolved_tensor = torch.Tensor.resolve_neg(input_tensor)
print('Resolved tensor: ', resolved_tensor)