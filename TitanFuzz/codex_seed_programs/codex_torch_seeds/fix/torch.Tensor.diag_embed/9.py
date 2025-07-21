'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.diag_embed\ntorch.Tensor.diag_embed(_input_tensor, offset=0, dim1=-2, dim2=-1)\n'
import torch
input_tensor = torch.randn(4, 4)
print('Input Tensor: \n', input_tensor)
output_tensor = input_tensor.diag_embed()
print('Output Tensor: \n', output_tensor)
output_tensor = input_tensor.diag_embed(offset=1)
print('Output Tensor: \n', output_tensor)
output_tensor = input_tensor.diag_embed(offset=2, dim1=0, dim2=1)
print('Output Tensor: \n', output_tensor)