"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Upsample\ntorch.nn.Upsample(size=None, scale_factor=None, mode='nearest', align_corners=None)\n"
import torch
import torch.nn as nn
import numpy as np
import torch
import torch.nn as nn
import numpy as np
input_tensor = torch.randn(1, 1, 2, 2)
upsample_tensor = nn.Upsample(size=(4, 4))
output_tensor = upsample_tensor(input_tensor)
print(output_tensor)
upsample_tensor = nn.Upsample(size=(4, 4), mode='bilinear')
output_tensor = upsample_tensor(input_tensor)
print(output_tensor)