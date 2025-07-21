'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tolist\ntorch.Tensor.tolist(_input_tensor)\n'
import torch
_input_tensor = torch.randn(3, 4)
_output_tensor = _input_tensor.tolist()
print(_output_tensor)