'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_and\ntorch.Tensor.bitwise_and(_input_tensor, other)\n'
import torch
input_tensor = torch.randint(0, 2, (4, 4), dtype=torch.uint8)
other = torch.randint(0, 2, (4, 4), dtype=torch.uint8)
result = input_tensor.bitwise_and(other)
print(input_tensor)
print(other)
print(result)