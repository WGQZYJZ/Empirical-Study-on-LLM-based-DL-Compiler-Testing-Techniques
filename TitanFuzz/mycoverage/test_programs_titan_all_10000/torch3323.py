import torch
from torch import nn
from torch.autograd import Variable
input_data = np.random.randn(2, 3, 4, 5, 6)
input_data = torch.tensor(input_data, dtype=torch.float)
dropout3d_op = torch.nn.Dropout3d(p=0.5, inplace=False)
output = dropout3d_op(input_data)