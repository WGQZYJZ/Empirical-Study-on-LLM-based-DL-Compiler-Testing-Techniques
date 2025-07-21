'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.apply_\ntorch.Tensor.apply_(_input_tensor, callable)\n'
import torch
input_tensor = torch.rand(10, 10)
output_tensor = torch.Tensor.apply_(input_tensor, (lambda x: (x * 2)))
print(output_tensor)