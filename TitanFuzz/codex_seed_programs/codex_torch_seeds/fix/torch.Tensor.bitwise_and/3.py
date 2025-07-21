'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_and\ntorch.Tensor.bitwise_and(_input_tensor, other)\n'
import torch
import torch
input_tensor = torch.randint(low=0, high=2, size=(4, 4), dtype=torch.int32)
other = torch.randint(low=0, high=2, size=(4, 4), dtype=torch.int32)
print('Input Tensor:')
print(input_tensor)
print('Other Tensor:')
print(other)
output_tensor = torch.Tensor.bitwise_and(input_tensor, other)
print('Output Tensor:')
print(output_tensor)