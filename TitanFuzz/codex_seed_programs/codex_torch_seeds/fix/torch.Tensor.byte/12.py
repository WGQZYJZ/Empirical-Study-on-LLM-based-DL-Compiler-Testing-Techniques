'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.byte\ntorch.Tensor.byte(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
input_tensor = torch.rand(4, 4)
print('input_tensor: ', input_tensor)
output_tensor = input_tensor.byte()
print('output_tensor: ', output_tensor)