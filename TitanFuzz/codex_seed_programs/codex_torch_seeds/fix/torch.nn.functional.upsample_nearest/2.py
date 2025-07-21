'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.upsample_nearest\ntorch.nn.functional.upsample_nearest(input, size=None, scale_factor=None)\n'
import torch
from torch.autograd import Variable
input_data = Variable(torch.Tensor([[[[1, 2], [3, 4]]]]))
output_data = torch.nn.functional.upsample_nearest(input_data, scale_factor=3)
print(output_data)