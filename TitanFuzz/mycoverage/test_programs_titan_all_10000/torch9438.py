import torch
from torch import nn
from torch.autograd import Variable
input_data = np.array([[3, 5], [5, 6], [7, 8]])
input_data = torch.tensor(input_data, dtype=torch.float32)
torch.hub.get_dir()