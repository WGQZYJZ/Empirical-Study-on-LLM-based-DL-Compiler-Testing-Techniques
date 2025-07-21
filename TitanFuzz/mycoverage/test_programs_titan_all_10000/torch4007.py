import torch
from torch import nn
from torch.autograd import Variable
input_data = np.array([[(- 1), (- 2), (- 3)], [3, 4, 5]])
input_data = torch.from_numpy(input_data).float()
output = torch.nn.functional.selu(input_data)