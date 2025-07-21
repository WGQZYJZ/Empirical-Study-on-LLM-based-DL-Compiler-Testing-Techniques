'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.int_repr\ntorch.Tensor.int_repr(_input_tensor)\n'
import torch
input_tensor = torch.randint(0, 10, (2, 3), dtype=torch.int32)
print('Input tensor: \n', input_tensor)
output_tensor = torch.Tensor.int_repr(input_tensor)
print('Output tensor: \n', output_tensor)