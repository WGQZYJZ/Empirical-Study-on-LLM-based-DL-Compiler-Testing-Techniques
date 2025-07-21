import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[0.1, 0.2, 0.3], [0.1, 0.2, 0.3]], dtype=torch.float32)
target_data = torch.tensor([[0.1, 0.2, 0.3], [0.1, 0.2, 0.3]], dtype=torch.float32)
output_data = torch.nn.functional.kl_div(input_data, target_data, reduction='batchmean')