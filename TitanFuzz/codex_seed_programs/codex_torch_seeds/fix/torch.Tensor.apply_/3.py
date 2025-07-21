'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.apply_\ntorch.Tensor.apply_(_input_tensor, callable)\n'
import torch
input_tensor = torch.randn(4, 4)
torch.Tensor.apply_(input_tensor, (lambda x: (x * 2)))
print(input_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.apply_\ntorch.Tensor.apply_(callable)\n'
import torch
input_tensor = torch.randn(4, 4)
input_tensor.apply_((lambda x: (x * 2)))
print(input_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.apply_\ntorch.Tensor.apply_(callable)\n'