import torch
from torch import nn
from torch.autograd import Variable
np.random.seed(0)
tensor1 = torch.tensor(np.random.randint(10, size=(3, 3)))
tensor2 = torch.tensor(np.random.randint(10, size=(3, 3)))
tensor3 = torch.tensor(np.random.randint(10, size=(3, 3)))
torch.Tensor.addcmul_(tensor1, tensor2, tensor3)