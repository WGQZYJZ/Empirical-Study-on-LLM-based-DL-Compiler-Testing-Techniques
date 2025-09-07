import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1000, 1000)
torch.set_num_threads(2)
start_time = time.time()
for i in range(100):
    torch.mm(input_data, input_data)
end_time = time.time()