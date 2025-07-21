'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_xor\ntorch.Tensor.bitwise_xor(_input_tensor, other)\n'
import torch
input_tensor = torch.randint(0, 2, (2, 3), dtype=torch.int8)
other = torch.randint(0, 2, (2, 3), dtype=torch.int8)
output_tensor = input_tensor.bitwise_xor(other)
print(input_tensor)
print(other)
print(output_tensor)