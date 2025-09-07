import torch
from torch import nn
from torch.autograd import Variable
input_data = [1, 2, 3]
tensor_data = torch.as_tensor(input_data)
numpy_data = np.array(input_data)
tensor_data = torch.from_numpy(numpy_data)
tensor_data = torch.ones(3)
tensor_data = torch.zeros(3)