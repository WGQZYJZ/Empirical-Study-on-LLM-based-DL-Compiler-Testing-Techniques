'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.pow\ntorch.Tensor.pow(_input_tensor, exponent)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
output_tensor = input_tensor.pow(2)
print(output_tensor)