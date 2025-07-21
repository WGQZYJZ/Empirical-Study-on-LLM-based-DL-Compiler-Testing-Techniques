import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[2.0, 1.0, 1.0], [1.0, 3.0, 2.0], [1.0, 0.0, 0.0]], dtype=torch.float32)
(LU_data, LU_pivots) = input_tensor.lu()
output_tensor = torch.Tensor.lu_solve(input_tensor, LU_data, LU_pivots)