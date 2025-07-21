'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isinf\ntorch.Tensor.isinf(_input_tensor)\n'
import torch
_input_tensor = torch.randn(1, 3, 3)
_result_tensor = torch.Tensor.isinf(_input_tensor)
print(_result_tensor)