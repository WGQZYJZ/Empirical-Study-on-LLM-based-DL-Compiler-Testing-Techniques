'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.matrix_power\ntorch.Tensor.matrix_power(_input_tensor, n)\n'
import torch
input_tensor = torch.tensor([[1, 2], [3, 4]])
print(input_tensor)
result = torch.Tensor.matrix_power(input_tensor, 2)
print(result)