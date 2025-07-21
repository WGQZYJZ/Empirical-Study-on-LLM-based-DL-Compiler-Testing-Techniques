import torch
from torch import nn
from torch.autograd import Variable
data = [1, 2, 3, 4]
tensor = torch.tensor(data)
tensor = torch.as_tensor(data)
tensor = torch.from_numpy(np.array(data))