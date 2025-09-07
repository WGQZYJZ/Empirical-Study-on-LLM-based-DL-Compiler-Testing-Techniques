import torch
from torch import nn
from torch.autograd import Variable
input_data = np.array([[3, 1], [1, 1], [1, 2], [2, 3]], dtype='float32')
input_data = Variable(torch.from_numpy(input_data))
url = 'https://s3.amazonaws.com/pytorch/models/resnet18-5c106cde.pth'
state_dict = torch.hub.load_state_dict_from_url(url)