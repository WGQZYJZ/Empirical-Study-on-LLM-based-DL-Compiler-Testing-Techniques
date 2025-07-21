'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nanmedian\ntorch.Tensor.nanmedian(_input_tensor, dim=None, keepdim=False)\n'
import torch
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float32)
print('input tensor: ', input_tensor)
output_tensor = torch.Tensor.nanmedian(input_tensor, dim=1, keepdim=True)
print('output tensor: ', output_tensor)