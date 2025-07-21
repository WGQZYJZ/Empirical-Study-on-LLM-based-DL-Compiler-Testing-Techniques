import torch
from torch import nn
from torch.autograd import Variable
input_tensor = np.random.randint(0, 100, size=100)
input_tensor = torch.from_numpy(input_tensor)
output_tensor = torch.Tensor.histc(input_tensor, bins=100, min=0, max=0)