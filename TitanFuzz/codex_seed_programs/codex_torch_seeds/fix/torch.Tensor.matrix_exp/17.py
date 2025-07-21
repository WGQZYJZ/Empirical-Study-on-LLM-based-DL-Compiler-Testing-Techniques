'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.matrix_exp\ntorch.Tensor.matrix_exp(_input_tensor)\n'
import torch
_input_tensor = torch.rand(2, 2)
_output_tensor = torch.Tensor.matrix_exp(_input_tensor)
print(_output_tensor)