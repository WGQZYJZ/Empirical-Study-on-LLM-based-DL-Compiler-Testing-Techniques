'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.std\ntorch.Tensor.std(_input_tensor, dim, unbiased=True, keepdim=False)\n'
import torch
input_tensor = torch.randn(2, 3)
print('input_tensor: ', input_tensor)
print('torch.Tensor.std(input_tensor, dim=0): ', torch.Tensor.std(input_tensor, dim=0))
print('torch.Tensor.std(input_tensor, dim=1): ', torch.Tensor.std(input_tensor, dim=1))
print('torch.Tensor.std(input_tensor, dim=1, unbiased=False): ', torch.Tensor.std(input_tensor, dim=1, unbiased=False))
print('torch.Tensor.std(input_tensor, dim=1, keepdim=True): ', torch.Tensor.std(input_tensor, dim=1, keepdim=True))