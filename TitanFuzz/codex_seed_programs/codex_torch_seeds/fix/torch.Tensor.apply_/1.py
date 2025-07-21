'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.apply_\ntorch.Tensor.apply_(_input_tensor, callable)\n'
import torch
input_tensor = torch.rand(2, 3)
print(input_tensor)
torch.Tensor.apply_(input_tensor, (lambda x: (x * 2)))
print(input_tensor)