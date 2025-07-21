'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isinf\ntorch.Tensor.isinf(_input_tensor)\n'
import torch
_input_tensor = torch.Tensor([float('inf'), float('-inf'), float('nan')])
_output_tensor = torch.Tensor.isinf(_input_tensor)
print(_output_tensor)