'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.resolve_neg\ntorch.Tensor.resolve_neg(_input_tensor)\n'
import torch
_input_tensor = torch.randn(3, 3)
_output_tensor = torch.Tensor.resolve_neg(_input_tensor)
print(_output_tensor)