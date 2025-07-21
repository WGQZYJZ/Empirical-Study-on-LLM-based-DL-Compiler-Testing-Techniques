'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.expand_as\ntorch.Tensor.expand_as(_input_tensor, other)\n'
import torch
input_tensor = torch.randint(low=0, high=10, size=(2, 3))
print(input_tensor)
other = torch.randint(low=0, high=10, size=(2, 3))
print(other)
output_tensor = input_tensor.expand_as(other)
print(output_tensor)