import torch
from torch import nn
from torch.autograd import Variable
data = np.random.randint(0, 100, (100,))
sampler = torch.utils.data.BatchSampler(data, batch_size=5, drop_last=True)
for i in sampler:
    print(i)