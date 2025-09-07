import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.randn(3, 3)
(eigen_values, eigen_vectors) = torch.symeig(input_data, eigenvectors=True)