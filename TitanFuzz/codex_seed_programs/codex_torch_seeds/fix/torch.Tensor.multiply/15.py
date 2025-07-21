'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.multiply\ntorch.Tensor.multiply(_input_tensor, value)\n'
import torch
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
output_tensor = input_tensor.multiply(2)
print(output_tensor)