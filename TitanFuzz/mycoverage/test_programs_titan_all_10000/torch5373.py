import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([(- 1.0), 1.0, 3.0, 5.0, (- 2.0), 1.0, 2.0, 3.0])
target_data = torch.tensor([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
huber_loss = torch.nn.HuberLoss(reduction='mean', delta=1.0)
output = huber_loss(input_data, target_data)