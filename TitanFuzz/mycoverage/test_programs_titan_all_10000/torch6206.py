import torch
from torch import nn
from torch.autograd import Variable
input_data = np.random.randn(1, 3, 32, 32, 32)
input_data = torch.from_numpy(input_data)
torch.nn.InstanceNorm3d(num_features=3, eps=1e-05, momentum=0.1, affine=False, track_running_stats=False, device=None, dtype=None)