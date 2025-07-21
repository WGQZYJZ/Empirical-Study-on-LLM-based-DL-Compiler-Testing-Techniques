'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.det\ntorch.Tensor.det(_input_tensor)\n'
import torch
_input_tensor = torch.randn(1, 2, 2)
_output_tensor = torch.Tensor.det(_input_tensor)
print(_output_tensor)