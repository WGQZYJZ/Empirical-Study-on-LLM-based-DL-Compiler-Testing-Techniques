'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.rrelu\ntorch.nn.functional.rrelu(input, lower=1./8, upper=1./3, training=False, inplace=False)\n'
import torch
from torch.autograd import Variable
import numpy as np
import torch
from torch.autograd import Variable
import numpy as np
input_data = Variable(torch.randn(1, 1, 3, 3))
output = torch.nn.functional.rrelu(input_data, lower=(1.0 / 8), upper=(1.0 / 3), training=False, inplace=False)
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.selu\ntorch.nn.functional.selu(input, alpha=1.6732632423543772848170429916717, scale=1.0507009873554804934193349852946, inplace=False)\n'
import torch
from torch.autograd import Variable
import numpy as np