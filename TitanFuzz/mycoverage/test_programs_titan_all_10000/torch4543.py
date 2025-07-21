import torch
from torch import nn
from torch.autograd import Variable
data = torch.randn(100, 3)
labels = torch.randint(0, 2, (100,))
dataloader = torch.utils.data.DataLoader(torch.utils.data.TensorDataset(data, labels), batch_size=10, shuffle=True, num_workers=2)
for (i, (batch_data, batch_labels)) in enumerate(dataloader):
    print(i, batch_data, batch_labels)