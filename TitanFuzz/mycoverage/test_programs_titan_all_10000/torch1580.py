import torch
from torch import nn
from torch.autograd import Variable
data_source = np.random.randint(0, 10, size=(100, 10))
sampler = torch.utils.data.SequentialSampler(data_source)
for i in sampler:
    print(i)