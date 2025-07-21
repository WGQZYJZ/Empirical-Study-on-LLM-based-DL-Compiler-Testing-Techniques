"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.kl_div\ntorch.nn.functional.kl_div(input, target, size_average=None, reduce=None, reduction='mean', log_target=False)\n"
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input_data = Variable(torch.Tensor([[1, 2, 4, 8], [1, 2, 4, 8]]))
target_data = Variable(torch.Tensor([[1, 2, 4, 8], [1, 2, 4, 8]]))
kl_div_loss = torch.nn.functional.kl_div(input_data, target_data)
print(kl_div_loss)