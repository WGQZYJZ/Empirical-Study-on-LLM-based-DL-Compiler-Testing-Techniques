'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_and_\ntorch.Tensor.bitwise_and_(_input_tensor, other)\n'
import torch
input_tensor = torch.randint(0, 2, (4, 4), dtype=torch.uint8)
print('Input Tensor:')
print(input_tensor)
other = torch.tensor([1, 1, 1, 1], dtype=torch.uint8)
output_tensor = input_tensor.bitwise_and_(other)
print('Output Tensor:')
print(output_tensor)