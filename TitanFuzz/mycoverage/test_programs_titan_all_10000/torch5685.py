import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(100, 100)
start = time.time()
futures = []
for i in range(0, 100):
    futures.append(torch.futures.Future())
for i in range(0, 100):
    futures[i].set_result(input_data[i])
end = time.time()