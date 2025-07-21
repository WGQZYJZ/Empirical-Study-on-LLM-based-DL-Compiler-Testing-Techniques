import torch
from torch import nn
from torch.autograd import Variable
input_data = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float32)
input_tensor = torch.Tensor(input_data)
output_tensor = torch.Tensor.double(input_tensor)