import torch
from torch import nn
from torch.autograd import Variable
input_data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
input_data = torch.tensor(input_data)
row = 3
col = 3
offset = 0
torch.tril_indices(row, col, offset=offset)