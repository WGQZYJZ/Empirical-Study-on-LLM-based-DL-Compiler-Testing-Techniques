import torch
from torch import nn
from torch.autograd import Variable
input_data = np.random.rand(1, 1, 5, 5, 5)
input_tensor = torch.from_numpy(input_data)
weight_data = np.random.rand(1, 1, 3, 3, 3)
weight_tensor = torch.from_numpy(weight_data)
output_tensor = torch.nn.functional.conv3d(input_tensor, weight_tensor)