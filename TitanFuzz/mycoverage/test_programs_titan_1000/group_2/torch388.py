import torch
from torch import nn
from torch.autograd import Variable
X = torch.rand(10, 2)
y = torch.rand(10, 1)
dataloader = torch.utils.data.DataLoader(torch.utils.data.TensorDataset(X, y), batch_size=4, shuffle=True, num_workers=4)
for (x_batch, y_batch) in dataloader:
    print(x_batch)
    print(y_batch)