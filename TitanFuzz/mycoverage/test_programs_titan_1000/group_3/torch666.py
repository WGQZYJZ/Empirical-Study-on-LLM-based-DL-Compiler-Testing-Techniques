import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor(np.random.rand(10, 1), dtype=torch.float32)
target = torch.tensor(np.random.randint(2, size=(10, 1)), dtype=torch.float32)
loss = torch.nn.functional.binary_cross_entropy_with_logits(input, target)