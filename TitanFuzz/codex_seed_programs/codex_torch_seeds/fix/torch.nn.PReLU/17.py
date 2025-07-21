'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.PReLU\ntorch.nn.PReLU(num_parameters=1, init=0.25, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
input_data = torch.from_numpy(np.array([[1, 2, 3], [4, 5, 6]])).float()
print('Input data: ', input_data)
model = nn.PReLU()
output = model(input_data)
print('Output: ', output)