import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randint(0, 255, (1, 3, 32, 32), dtype=torch.uint8)
torch.Tensor.q_per_channel_axis(_input_tensor)