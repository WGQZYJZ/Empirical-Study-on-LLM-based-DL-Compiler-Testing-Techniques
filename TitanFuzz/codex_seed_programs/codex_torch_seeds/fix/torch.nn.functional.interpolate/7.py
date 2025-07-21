"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.interpolate\ntorch.nn.functional.interpolate(input, size=None, scale_factor=None, mode='nearest', align_corners=None, recompute_scale_factor=None)\n"
import torch
import torch.nn.functional as F
import numpy as np
import torch
import torch.nn.functional as F
import numpy as np
input_data = torch.tensor(np.random.rand(1, 3, 5, 5), dtype=torch.float32)
print('Input data: ', input_data)
output_data = F.interpolate(input_data, scale_factor=2, mode='nearest')
print('Output data: ', output_data)