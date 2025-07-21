'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.PixelUnshuffle\ntorch.nn.PixelUnshuffle(downscale_factor)\n'
import torch
import numpy as np
from torch.autograd import Variable
import torch
import numpy as np
from torch.autograd import Variable
input = np.random.rand(1, 1, 4, 4)
input = Variable(torch.from_numpy(input))
pixel_unshuffle = torch.nn.PixelUnshuffle(2)
output = pixel_unshuffle(input)
print(input)
print(output)