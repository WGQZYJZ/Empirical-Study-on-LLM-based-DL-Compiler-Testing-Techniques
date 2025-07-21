'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.retains_grad\ntorch.Tensor.retains_grad(_input_tensor, )\n'
import torch
input_tensor = torch.randn(2, 3)
retains_grad_result = torch.Tensor.retains_grad(input_tensor, True)
print('retains_grad_result: ', retains_grad_result)