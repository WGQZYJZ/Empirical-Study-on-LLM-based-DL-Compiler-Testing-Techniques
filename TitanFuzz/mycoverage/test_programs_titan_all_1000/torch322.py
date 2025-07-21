import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(3, 3)
corr_cholesky = torch.distributions.transforms.CorrCholeskyTransform(cache_size=0)
output_data = corr_cholesky(input_data)
corr_cholesky.inv(output_data)