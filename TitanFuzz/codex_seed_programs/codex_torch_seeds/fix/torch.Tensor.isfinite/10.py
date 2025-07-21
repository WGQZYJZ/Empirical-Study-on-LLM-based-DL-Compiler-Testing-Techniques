'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isfinite\ntorch.Tensor.isfinite(_input_tensor)\n'
import torch
_input_tensor = torch.randn(4, 4)
_input_tensor[0][0] = float('nan')
_input_tensor[1][1] = float('inf')
_input_tensor[2][2] = float('-inf')
print(_input_tensor.isfinite())