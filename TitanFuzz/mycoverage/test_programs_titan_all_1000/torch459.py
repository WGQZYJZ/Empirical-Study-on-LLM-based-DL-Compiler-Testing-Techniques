import torch
from torch import nn
from torch.autograd import Variable
x_data = torch.tensor(np.random.random((5, 10)), dtype=torch.float32)
y_data = torch.tensor(np.random.randint(2, size=(5, 10)), dtype=torch.float32)
loss = torch.nn.functional.binary_cross_entropy_with_logits(x_data, y_data)