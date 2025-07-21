'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.matrix_power\ntorch.Tensor.matrix_power(_input_tensor, n)\n'
import torch
import torch
_input_tensor = torch.rand(3, 3, dtype=torch.float)
result = _input_tensor.matrix_power(2)
print(result)