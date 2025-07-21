import torch
from torch import nn
from torch.autograd import Variable
data = torch.randn(5, 3)
loader = torch.utils.data.DataLoader(data, batch_size=2, shuffle=True, num_workers=2)
for (i, batch_data) in enumerate(loader):
    print(i, batch_data)