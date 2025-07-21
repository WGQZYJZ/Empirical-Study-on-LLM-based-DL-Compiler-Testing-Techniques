"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Upsample\ntorch.nn.Upsample(size=None, scale_factor=None, mode='nearest', align_corners=None)\n"
import torch
import torch.nn as nn
import numpy as np
import torch
import torch.nn as nn
import numpy as np
input_data = np.random.rand(1, 1, 2, 2)
input_data = torch.from_numpy(input_data)
upsample = nn.Upsample(size=(3, 3), mode='nearest')
output = upsample(input_data)
print(output)