import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(5, 3)
dataloader = torch.utils.data.DataLoader(input_data, batch_size=2, shuffle=True)
for (batch_idx, batch_data) in enumerate(dataloader):
    print('batch_idx: ', batch_idx)
    print('batch_data: ', batch_data)
    print('')