import torch
from torch import nn
from torch.autograd import Variable

data = np.array([[(- 1), 1, (- 0.5), 0.5, 0]])
x = torch.from_numpy(data)
y = torch.nn.Softsign()