"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.interpolate\ntorch.nn.functional.interpolate(input, size=None, scale_factor=None, mode='nearest', align_corners=None, recompute_scale_factor=None)\n"
import torch
import numpy as np
import math
import torch.nn.functional as F
import torch
import numpy as np
import math
import torch.nn.functional as F
input_data = torch.arange(0, 16, dtype=torch.float32).reshape(1, 1, 4, 4)
output = F.interpolate(input_data, scale_factor=2, mode='bilinear', align_corners=True)
print(input_data)
print(output)