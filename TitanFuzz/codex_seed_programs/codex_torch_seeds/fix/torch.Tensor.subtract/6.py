'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.subtract\ntorch.Tensor.subtract(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.randint(10, (3, 3))
print(input_tensor)
output_tensor = input_tensor.subtract(5)
print(output_tensor)
output_tensor = input_tensor.subtract(5, alpha=2)
print(output_tensor)