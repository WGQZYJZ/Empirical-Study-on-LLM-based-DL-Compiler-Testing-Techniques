'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_and\ntorch.Tensor.bitwise_and(_input_tensor, other)\n'
import torch
input_tensor = torch.randint(low=0, high=2, size=(3, 4), dtype=torch.int8)
other = torch.randint(low=0, high=2, size=(3, 4), dtype=torch.int8)
output_tensor = input_tensor.bitwise_and(other)
print(output_tensor)