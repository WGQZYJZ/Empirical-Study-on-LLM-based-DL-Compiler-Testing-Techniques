import torch
from torch import nn
from torch.autograd import Variable
x = np.random.rand(10, 3, 10)
x = torch.tensor(x, dtype=torch.float32)
torch.nn.InstanceNorm1d(num_features=3, eps=1e-05, momentum=0.1, affine=False, track_running_stats=False)