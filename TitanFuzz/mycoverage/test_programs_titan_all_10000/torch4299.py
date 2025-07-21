import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]], dtype=torch.float32, requires_grad=True)
torch.get_num_threads()
torch.set_num_threads(1)