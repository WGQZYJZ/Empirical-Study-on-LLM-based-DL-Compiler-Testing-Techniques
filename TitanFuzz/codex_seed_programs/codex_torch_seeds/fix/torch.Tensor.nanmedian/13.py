'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nanmedian\ntorch.Tensor.nanmedian(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_data = torch.randn(2, 3, 3)
print('Input data: \n', input_data)
print('\nMedian along dimension 0: \n', torch.Tensor.nanmedian(input_data, dim=0))
print('\nMedian along dimension 1: \n', torch.Tensor.nanmedian(input_data, dim=1))
print('\nMedian along dimension 2: \n', torch.Tensor.nanmedian(input_data, dim=2))
print('\nMedian along all dimensions: \n', torch.Tensor.nanmedian(input_data, dim=None))
print('\nMedian along dimension 0 with keepdim: \n', torch.Tensor.nanmedian(input_data, dim=0, keepdim=True))