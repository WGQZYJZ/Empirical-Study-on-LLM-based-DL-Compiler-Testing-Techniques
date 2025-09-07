import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[(- 1), (- 2), (- 3)], [1, 2, 3]], dtype=torch.float32)
output_tensor = torch.Tensor.negative_(input_tensor)