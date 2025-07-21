'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.diag_embed\ntorch.Tensor.diag_embed(_input_tensor, offset=0, dim1=-2, dim2=-1)\n'
import torch
input_tensor = torch.randn((2, 3, 4, 5))
result = torch.Tensor.diag_embed(input_tensor, offset=0, dim1=(- 2), dim2=(- 1))
print(result)