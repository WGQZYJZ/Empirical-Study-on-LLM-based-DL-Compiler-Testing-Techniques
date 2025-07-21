'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.kthvalue\ntorch.Tensor.kthvalue(_input_tensor, k, dim=None, keepdim=False)\n'
import torch
import torch
input_tensor = torch.randn(10, 3)
kth_value = input_tensor.kthvalue(1, dim=1, keepdim=True)
print('kth_value:', kth_value)