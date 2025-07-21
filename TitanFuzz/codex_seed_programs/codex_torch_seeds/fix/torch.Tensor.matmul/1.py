'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.matmul\ntorch.Tensor.matmul(_input_tensor, tensor2)\n'
import torch
input_tensor = torch.randn(1, 3, 1, 1)
tensor2 = torch.randn(1, 3, 1, 1)
output_tensor = torch.Tensor.matmul(input_tensor, tensor2)
print(output_tensor)