import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(100, 100)
torch.set_num_interop_threads(1)
start = time.time()
result = torch.matmul(input_data, input_data)
end = time.time()