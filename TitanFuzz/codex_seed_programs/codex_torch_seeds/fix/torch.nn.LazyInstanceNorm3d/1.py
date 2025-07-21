'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LazyInstanceNorm3d\ntorch.nn.LazyInstanceNorm3d(eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input_data = torch.randn(1, 3, 5, 5, 5)
print('Task 3: Call the API torch.nn.LazyInstanceNorm3d')
lazy_instance_norm_3d = torch.nn.LazyInstanceNorm3d(eps=1e-05, momentum=0.1, affine=True, track_running_stats=True, device=None, dtype=None)
output_data = lazy_instance_norm_3d(input_data)
print('input_data: ', input_data)
print('output_data: ', output_data)