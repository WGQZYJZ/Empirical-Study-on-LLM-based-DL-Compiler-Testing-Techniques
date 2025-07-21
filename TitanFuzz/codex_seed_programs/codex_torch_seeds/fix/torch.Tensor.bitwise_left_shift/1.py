'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_left_shift\ntorch.Tensor.bitwise_left_shift(_input_tensor, other)\n'
import torch
input_tensor = torch.randint(low=0, high=10, size=(4, 4), dtype=torch.int32)
print('Input Tensor:')
print(input_tensor)
other = torch.randint(low=0, high=10, size=(4, 4), dtype=torch.int32)
print('Other Tensor:')
print(other)
output_tensor = torch.Tensor.bitwise_left_shift(input_tensor, other)
print('Output Tensor:')
print(output_tensor)