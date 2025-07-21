'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.retains_grad\ntorch.Tensor.retains_grad(_input_tensor, )\n'
import torch
_input_tensor = torch.rand(2, 3)
print('Input tensor: ', _input_tensor)
torch.Tensor.retains_grad(_input_tensor, True)
print('Input tensor retains_grad: ', _input_tensor.retains_grad)