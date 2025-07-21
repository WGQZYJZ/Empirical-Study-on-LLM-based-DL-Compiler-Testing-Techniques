import torch
from torch import nn
from torch.autograd import Variable
input_data = np.random.randn(2, 3)
input_data = torch.tensor(input_data, dtype=torch.float)
output_data = torch.nn.functional.softsign(input_data)