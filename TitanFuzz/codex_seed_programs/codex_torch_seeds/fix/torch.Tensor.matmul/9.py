'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.matmul\ntorch.Tensor.matmul(_input_tensor, tensor2)\n'
import torch
input_tensor = torch.randn(3, 5)
tensor2 = torch.randn(5, 4)
result = torch.Tensor.matmul(input_tensor, tensor2)
print(result)