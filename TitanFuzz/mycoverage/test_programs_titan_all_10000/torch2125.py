import torch
from torch import nn
from torch.autograd import Variable
input_data = np.random.rand(1, 3, 3)
input_data = torch.from_numpy(input_data)
output = torch.special.erfcx(input_data)