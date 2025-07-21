import torch
from torch import nn
from torch.autograd import Variable
input_data = np.random.rand(10, 10)
tanh_transform = torch.distributions.transforms.TanhTransform()
output = tanh_transform(torch.tensor(input_data))