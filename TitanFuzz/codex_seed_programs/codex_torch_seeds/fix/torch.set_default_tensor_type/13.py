'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_default_tensor_type\ntorch.set_default_tensor_type(t)\n'
import torch
from torch.autograd import Variable
input_data = Variable(torch.randn(2, 3, 3))
target_data = Variable(torch.randn(2, 3, 3))
torch.set_default_tensor_type(torch.FloatTensor)