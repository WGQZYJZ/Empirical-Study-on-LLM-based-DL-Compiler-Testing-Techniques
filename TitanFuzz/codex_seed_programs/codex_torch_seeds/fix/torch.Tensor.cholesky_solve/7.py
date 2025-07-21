'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cholesky_solve\ntorch.Tensor.cholesky_solve(_input_tensor, input2, upper=False)\n'
import torch
batch_size = 10
input_size = (batch_size, 3, 3)
input_tensor = torch.rand(input_size)
input2 = torch.rand(batch_size, 3)
output_tensor = input_tensor.cholesky_solve(input2)
print('input_tensor: ', input_tensor)
print('input2: ', input2)
print('output_tensor: ', output_tensor)