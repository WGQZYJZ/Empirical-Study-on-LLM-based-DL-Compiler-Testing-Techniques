import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor(np.random.random((2, 3)), dtype=torch.float32)
output = torch.nn.functional.relu(input_data)