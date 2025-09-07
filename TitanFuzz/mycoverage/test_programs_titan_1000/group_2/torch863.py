import torch
from torch import nn
from torch.autograd import Variable
url = 'https://download.pytorch.org/models/resnet18-5c106cde.pth'
state_dict = torch.hub.load_state_dict_from_url(url)