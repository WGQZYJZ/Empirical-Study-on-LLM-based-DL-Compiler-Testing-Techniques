import torch
from torch import nn
from torch.autograd import Variable
input_data = Variable(torch.Tensor(np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]])))
max_pooling_layer = torch.nn.MaxPool1d(2, stride=2)
output = max_pooling_layer(input_data)