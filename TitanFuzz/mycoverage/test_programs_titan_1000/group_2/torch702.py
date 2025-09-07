import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0], [7.0, 8.0], [9.0, 10.0], [11.0, 12.0]])
futures = [torch.futures.Future(), torch.futures.Future()]
futures[0].set_result(input_data[:3])
futures[1].set_result(input_data[3:])
result = torch.futures.wait_all(futures)