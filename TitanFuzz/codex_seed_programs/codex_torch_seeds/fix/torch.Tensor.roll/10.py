'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.roll\ntorch.Tensor.roll(_input_tensor, shifts, dims)\n'
import torch
input_tensor = torch.Tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
output_tensor = torch.Tensor.roll(input_tensor, shifts=1, dims=1)
print('input_tensor:')
print(input_tensor)
print('output_tensor:')
print(output_tensor)