import torch
from torch import nn
from torch.autograd import Variable
input_size = (1, 1, 4)
input_data = np.array([[1, 2, 3, 4]], dtype=np.float32)
input_data = torch.from_numpy(input_data)
input_data = input_data.view(input_size)
output = torch.nn.functional.max_pool1d(input_data, kernel_size=2)