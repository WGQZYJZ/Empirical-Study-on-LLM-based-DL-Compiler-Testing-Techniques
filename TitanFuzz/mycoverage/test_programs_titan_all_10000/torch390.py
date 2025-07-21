import torch
from torch import nn
from torch.autograd import Variable
data = [[1, 2, 3], [4, 5, 6]]
torch.get_default_dtype()
torch.tensor(data)
torch.as_tensor(data)
np_data = np.array(data)
torch.from_numpy(np_data)
torch.eye(2)
torch.zeros(2, 3)
torch.ones(2, 3)
torch.rand(2, 3)