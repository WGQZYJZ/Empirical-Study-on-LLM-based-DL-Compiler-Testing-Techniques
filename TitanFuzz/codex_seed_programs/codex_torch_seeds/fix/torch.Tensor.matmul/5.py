'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.matmul\ntorch.Tensor.matmul(_input_tensor, tensor2)\n'
import torch
input_tensor = torch.randn(2, 3)
tensor2 = torch.randn(3, 4)
output_tensor = input_tensor.matmul(tensor2)
print(output_tensor)