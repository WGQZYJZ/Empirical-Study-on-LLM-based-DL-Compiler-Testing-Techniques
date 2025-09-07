import torch
from torch import nn
from torch.autograd import Variable

_input_data = np.array([[0, (- 1)], [1, (- 2)], [(- 1), 1], [2, 1]])
_input_tensor = torch.from_numpy(_input_data)
_output_tensor = torch.Tensor.tanh(_input_tensor)