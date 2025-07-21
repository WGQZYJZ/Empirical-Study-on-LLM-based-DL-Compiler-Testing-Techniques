'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cos\ntorch.Tensor.cos(_input_tensor)\n'
import torch
_input_tensor = torch.rand(1000)
output_tensor = torch.Tensor.cos(_input_tensor)
print(output_tensor)