import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([1.2, 2.3, 3.4, 4.5, 5.6, 6.7, 7.8, 8.9, 9.0])
boundaries = torch.tensor([2, 4, 6, 8])
result = torch.bucketize(input, boundaries, out_int32=True, right=False)
input = torch.tensor([1.2, 2.3, 3.4, 4.5, 5.6, 6.7, 7.8, 8.9, 9.0])
boundaries = torch.tensor([2, 4, 6, 8])
result = torch.bucketize(input, boundaries, out_int32=True, right=True)