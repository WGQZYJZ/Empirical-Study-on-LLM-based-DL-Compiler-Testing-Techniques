'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.fractional_max_pool3d\ntorch.nn.functional.fractional_max_pool3d(*args, **kwargs)\n'
import torch
from torch.autograd import Variable
from torch.nn.functional import fractional_max_pool3d
import torch
input_data = torch.randn(1, 1, 5, 5, 5)
output = fractional_max_pool3d(input_data, (2, 2, 2), output_size=(2, 2, 2))
print(output)