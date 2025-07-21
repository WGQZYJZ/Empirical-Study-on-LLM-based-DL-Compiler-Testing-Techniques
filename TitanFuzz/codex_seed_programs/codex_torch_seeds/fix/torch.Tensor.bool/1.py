'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bool\ntorch.Tensor.bool(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
input_tensor = torch.randn(20, 20, dtype=torch.float32)
output_tensor = input_tensor.bool()
print('The input tensor is: ', input_tensor)
print('The output tensor is: ', output_tensor)