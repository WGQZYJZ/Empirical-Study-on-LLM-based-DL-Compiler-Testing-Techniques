'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.resolve_conj\ntorch.Tensor.resolve_conj(_input_tensor)\n'
import torch
import numpy as np
_input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
_output_tensor = torch.Tensor.resolve_conj(_input_tensor)
print(_output_tensor)