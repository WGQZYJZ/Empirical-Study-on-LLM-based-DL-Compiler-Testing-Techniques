import torch
from torch import nn
from torch.autograd import Variable
data = [[1, 2], [3, 4]]
tensor = torch.tensor(data)
data = [[1, 2], [3, 4]]
tensor = torch.as_tensor(data)
data = np.array([[1, 2], [3, 4]])
tensor = torch.from_numpy(data)
tensor = torch.eye(2)