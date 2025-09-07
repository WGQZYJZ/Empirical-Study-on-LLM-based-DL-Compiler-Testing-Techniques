import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([[4.0, 1.0, 1.0], [1.0, 2.0, 1.0], [1.0, 1.0, 2.0]])
output = torch.cholesky(input)
y = torch.randn(3, 2)
x = torch.cholesky_solve(y, output)
output_inverse = torch.cholesky_inverse(output)
output_inverse_solve = torch.cholesky_inverse(output, upper=True)