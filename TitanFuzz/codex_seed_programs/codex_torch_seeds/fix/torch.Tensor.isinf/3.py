'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isinf\ntorch.Tensor.isinf(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3, 4)
input_tensor[(0, 0, 0)] = float('inf')
input_tensor[(1, 2, 3)] = float('-inf')
output_tensor = torch.Tensor.isinf(input_tensor)
print('output_tensor: ', output_tensor)