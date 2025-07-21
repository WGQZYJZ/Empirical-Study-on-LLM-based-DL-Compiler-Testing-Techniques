'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.vsplit\ntorch.Tensor.vsplit(_input_tensor, split_size_or_sections)\n'
import torch
_input_tensor = torch.Tensor([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])
_output_tensor = torch.Tensor.vsplit(_input_tensor, 2)
print(_output_tensor)