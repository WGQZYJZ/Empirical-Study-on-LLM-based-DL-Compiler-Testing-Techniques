'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.q_per_channel_scales\ntorch.Tensor.q_per_channel_scales(_input_tensor)\n'
import torch
from torch.autograd import Variable
import numpy as np
import torch
from torch.autograd import Variable
import numpy as np
input_tensor = Variable(torch.randn(1, 3, 224, 224).cuda(), requires_grad=True)
torch.Tensor.q_per_channel_scales(input_tensor)