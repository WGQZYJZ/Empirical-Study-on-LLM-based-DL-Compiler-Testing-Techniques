'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.diag_embed\ntorch.Tensor.diag_embed(_input_tensor, offset=0, dim1=-2, dim2=-1)\n'
import torch
input_data = torch.randn(2, 3)
print(input_data)
output_data = torch.Tensor.diag_embed(input_data, offset=0, dim1=(- 2), dim2=(- 1))
print(output_data)