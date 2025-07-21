'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.matrix_power\ntorch.Tensor.matrix_power(_input_tensor, n)\n'
import torch
import torch
input_tensor = torch.Tensor([[1, 2], [3, 4]])
result = input_tensor.matrix_power(2)
print(result)
'\nExpected output:\ntensor([[ 7., 10.],\n        [15., 22.]])\n'