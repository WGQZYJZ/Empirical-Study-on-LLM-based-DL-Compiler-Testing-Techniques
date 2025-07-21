import torch
from torch import nn
from torch.autograd import Variable
x_data = Variable(torch.Tensor([[1.0], [2.0], [3.0]]))
y_data = Variable(torch.Tensor([[2.0], [4.0], [6.0]]))
url = 'https://download.pytorch.org/models/resnet18-5c106cde.pth'
model = torch.hub.load_state_dict_from_url(url)