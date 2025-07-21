'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.einsum\ntorch.einsum(equation, *operands)\n'
import torch
input_data = torch.rand(3, 4, 5)
print('input_data: ', input_data)
output_data = torch.einsum('ijk, ilk -> ijl', input_data, input_data)
print('output_data: ', output_data)