'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LPPool1d\ntorch.nn.LPPool1d(norm_type, kernel_size, stride=None, ceil_mode=False)\n'
import torch
from torch.autograd import Variable
import numpy as np
import torch
from torch.autograd import Variable
import numpy as np
np_data = np.random.rand(10, 3, 7)
torch_data = torch.from_numpy(np_data)
variable_data = Variable(torch_data)
pooling_layer = torch.nn.LPPool1d(2, 3, stride=None, ceil_mode=False)
pooling_layer(variable_data).data.numpy()