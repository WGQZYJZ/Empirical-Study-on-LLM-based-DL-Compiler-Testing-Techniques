'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.constant_\ntorch.nn.init.constant_(tensor, val)\n'
import torch
import numpy as np
import torch
import numpy as np
input_data = np.array([[1, 2, 3], [4, 5, 6]])
input_data = torch.from_numpy(input_data)
print(input_data)
torch.nn.init.constant_(input_data, val=0)
print(input_data)
torch.nn.init.constant_(input_data, val=1)
print(input_data)
torch.nn.init.constant_(input_data, val=2)
print(input_data)
torch.nn.init.constant_(input_data, val=3)