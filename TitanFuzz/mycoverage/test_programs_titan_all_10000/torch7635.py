import torch
from torch import nn
from torch.autograd import Variable
x = np.random.rand(10, 3)
x_tensor = torch.from_numpy(x)
x_tensor2 = torch.tensor(x)
x_tensor3 = torch.as_tensor(x)
x_tensor4 = torch.from_numpy(x.astype(np.int32))