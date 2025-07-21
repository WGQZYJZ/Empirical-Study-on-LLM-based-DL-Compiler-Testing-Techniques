import torch
from torch import nn
from torch.autograd import Variable
input_data = np.array([[1, 2, 3], [4, 5, 6]])
input_data = torch.from_numpy(input_data)
out = torch.special.entr(input_data)