'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fake_quantize_per_tensor_affine\ntorch.fake_quantize_per_tensor_affine(input, scale, zero_point, quant_min, quant_max)\n'
import torch
from torch.autograd import Variable
import numpy as np
import torch
from torch.autograd import Variable
import numpy as np
input = Variable(torch.FloatTensor([[(- 63.0), (- 127.0), 63.0, 127.0]]))
output = torch.fake_quantize_per_tensor_affine(input, scale=1.0, zero_point=0, quant_min=0, quant_max=255)
print('input:', input)
print('output:', output)
'\nResult:\ninput: tensor([[-63., -127.,   63.,  127.]])\noutput: tensor([[  0.,    0.,  255.,  255.]])\n'