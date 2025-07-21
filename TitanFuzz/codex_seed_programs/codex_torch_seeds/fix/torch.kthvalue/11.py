'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.kthvalue\ntorch.kthvalue(input, k, dim=None, keepdim=False, *, out=None)\n'
import torch
input_tensor = torch.randn(3, 4)
print('Input tensor:')
print(input_tensor)
(kth_value, kth_index) = torch.kthvalue(input_tensor, 2, dim=1)
print('\nkth value:')
print(kth_value)
print('\nkth index:')
print(kth_index)
(kth_value, kth_index) = torch.kthvalue(input_tensor, 3, dim=1)
print('\nkth value:')
print(kth_value)
print('\nkth index:')
print(kth_index)
(kth_value, kth_index) = torch.kthvalue(input_tensor, 4, dim=1)
print('\nkth value:')
print