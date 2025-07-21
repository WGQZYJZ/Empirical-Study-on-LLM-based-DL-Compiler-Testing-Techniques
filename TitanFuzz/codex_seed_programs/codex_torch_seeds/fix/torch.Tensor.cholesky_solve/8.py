'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cholesky_solve\ntorch.Tensor.cholesky_solve(_input_tensor, input2, upper=False)\n'
import torch
input_tensor = torch.tensor([[4.0, 6.0], [6.0, 10.0]])
input2 = torch.tensor([[2.0], [3.0]])
torch.Tensor.cholesky_solve(input_tensor, input2, upper=False)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.inverse\ntorch.Tensor.inverse(_input_tensor)\n'
import torch
input_tensor = torch.tensor([[4.0, 6.0], [6.0, 10.0]])
torch.Tensor.inverse(input_tensor)