import torch
from torch import nn
from torch.autograd import Variable
input_data = np.array([[1, 2, 3], [4, 5, 6]])
input_tensor = torch.tensor(input_data)
output_tensor = torch.Tensor.is_meta(input_tensor)