import torch
from torch import nn
from torch.autograd import Variable
input_data = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
input_data_tensor = torch.from_numpy(input_data)
input_data_tensor = torch.tensor(input_data)