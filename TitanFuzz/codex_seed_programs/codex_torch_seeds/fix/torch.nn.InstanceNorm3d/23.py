'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.InstanceNorm3d\ntorch.nn.InstanceNorm3d(num_features, eps=1e-05, momentum=0.1, affine=False, track_running_stats=False, device=None, dtype=None)\n'
import torch
from torch.autograd import Variable
input_data = Variable(torch.randn(1, 4, 3, 3, 3))
norm = torch.nn.InstanceNorm3d(4)
output_data = norm(input_data)
print('input_data:', input_data)
print('output_data:', output_data)