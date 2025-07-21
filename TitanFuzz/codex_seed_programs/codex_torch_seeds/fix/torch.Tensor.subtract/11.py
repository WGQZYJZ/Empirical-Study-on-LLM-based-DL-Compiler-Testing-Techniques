'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.subtract\ntorch.Tensor.subtract(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
other = torch.tensor([[10, 20, 30], [40, 50, 60]])
output_tensor = torch.Tensor.subtract(input_tensor, other)
print(output_tensor)
output_tensor = torch.Tensor.subtract(input_tensor, other, alpha=0.5)
print(output_tensor)
output_tensor = torch.Tensor.subtract(input_tensor, other, alpha=2)
print(output_tensor)