import torch
from torch import nn
from torch.autograd import Variable
input_data = np.random.rand(3, 4).astype(np.float32)
input_data = torch.from_numpy(input_data)
output_data = torch.special.digamma(input_data)