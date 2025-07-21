'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.matrix_power\ntorch.Tensor.matrix_power(_input_tensor, n)\n'
import torch
_input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
_output_tensor = _input_tensor.matrix_power(3)
print(_output_tensor)