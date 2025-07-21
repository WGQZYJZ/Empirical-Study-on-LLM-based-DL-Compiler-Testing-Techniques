'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.greater\ntorch.Tensor.greater(_input_tensor, other)\n'
import torch
import torch
input_tensor = torch.rand(3, 3)
print(input_tensor)
output_tensor = torch.Tensor.greater(input_tensor, 0.5)
print(output_tensor)