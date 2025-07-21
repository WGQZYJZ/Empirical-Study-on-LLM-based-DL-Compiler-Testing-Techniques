'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.grad\ntorch.Tensor.grad(_input_tensor, )\n'
import torch
_input_tensor = torch.Tensor([[1, 2], [3, 4]])
_grad_output = torch.Tensor([[1, 1], [1, 1]])
_grad_output_tensor = torch.Tensor.grad(_input_tensor, _grad_output)
print(_grad_output_tensor)