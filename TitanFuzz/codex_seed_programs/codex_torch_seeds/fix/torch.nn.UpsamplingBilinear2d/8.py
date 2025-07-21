'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.UpsamplingBilinear2d\ntorch.nn.UpsamplingBilinear2d(size=None, scale_factor=None)\n'
import torch
import numpy as np
import torch
input_data = torch.tensor(np.random.rand(1, 1, 4, 4), dtype=torch.float32)
output = torch.nn.UpsamplingBilinear2d(size=None, scale_factor=2)(input_data)
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.UpsamplingNearest2d\ntorch.nn.UpsamplingNearest2d(size=None, scale_factor=None)\n'
import torch
import numpy as np
import torch
input_data = torch.tensor(np.random.rand(1, 1, 4, 4), dtype=torch.float32)
output = torch.nn.UpsamplingNearest2d(size=None, scale_factor=2)(input_data)
print