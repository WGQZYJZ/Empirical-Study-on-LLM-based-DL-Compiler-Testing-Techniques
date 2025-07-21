import torch
from torch import nn
from torch.autograd import Variable
input_data = [1, 2, 3, 4, 5]
long_storage = torch.LongStorage(input_data)
long_storage = torch.LongStorage(input_data).tolist()
long_storage = torch.LongStorage(input_data).size()
long_storage = torch.LongStorage(input_data).element_size()
long_storage = torch.LongStorage(input_data).data_ptr()
long_storage