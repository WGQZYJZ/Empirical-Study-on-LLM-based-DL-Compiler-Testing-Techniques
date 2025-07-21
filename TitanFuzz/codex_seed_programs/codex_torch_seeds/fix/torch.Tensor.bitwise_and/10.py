'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_and\ntorch.Tensor.bitwise_and(_input_tensor, other)\n'
import torch
input_tensor = torch.randint(0, 2, (2, 3), dtype=torch.uint8)
print('input tensor:', input_tensor)
output_tensor = input_tensor.bitwise_and(torch.ones((2, 3), dtype=torch.uint8))
print('output tensor:', output_tensor)