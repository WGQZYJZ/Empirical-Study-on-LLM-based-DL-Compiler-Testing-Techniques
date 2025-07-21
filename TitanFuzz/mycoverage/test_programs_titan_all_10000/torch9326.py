import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([1, 2, 3, 4, 5])
url = 'https://download.pytorch.org/models/resnet18-5c106cde.pth'
model = torch.hub.load_state_dict_from_url(url)