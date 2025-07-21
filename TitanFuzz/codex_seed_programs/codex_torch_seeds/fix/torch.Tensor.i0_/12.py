'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.i0_\ntorch.Tensor.i0_(_input_tensor)\n'
import torch
input_tensor = torch.tensor([[1.0, 2.0, 3.0, 4.0], [5.0, 6.0, 7.0, 8.0], [9.0, 10.0, 11.0, 12.0]])
output_tensor = torch.Tensor.i0_(input_tensor)
print('input_tensor:')
print(input_tensor)
print('output_tensor:')
print(output_tensor)