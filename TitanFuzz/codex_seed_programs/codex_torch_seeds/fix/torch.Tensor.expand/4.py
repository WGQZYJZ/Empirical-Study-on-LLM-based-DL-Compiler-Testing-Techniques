'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.expand\ntorch.Tensor.expand(_input_tensor, *sizes)\n'
import torch
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
print(input_tensor)
output_tensor = input_tensor.expand(4, 6)
print(output_tensor)