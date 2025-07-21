'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.retains_grad\ntorch.Tensor.retains_grad(_input_tensor, )\n'
import torch
input_tensor = torch.randn(1, requires_grad=True)
torch.Tensor.retains_grad(input_tensor, True)
print('The input tensor is: ', input_tensor)
print("The input tensor's retain_grad is: ", input_tensor.retains_grad)