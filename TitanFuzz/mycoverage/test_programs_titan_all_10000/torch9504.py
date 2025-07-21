import torch
from torch import nn
from torch.autograd import Variable
data = [[1, 2], [3, 4]]
tensor = torch.as_tensor(data, dtype=None, device=None)
array = np.array([[1, 2], [3, 4]])
tensor = torch.from_numpy(array)
tensor = torch.eye(2, 3)
tensor = torch.zeros(2, 3)