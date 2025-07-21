'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.lt\ntorch.Tensor.lt(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([[1, 2], [3, 4]])
output_tensor = input_tensor.lt(3)
print(output_tensor)
print(type(output_tensor))