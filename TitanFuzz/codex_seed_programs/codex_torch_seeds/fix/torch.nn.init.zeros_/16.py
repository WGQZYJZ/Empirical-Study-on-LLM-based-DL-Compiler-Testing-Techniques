'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.zeros_\ntorch.nn.init.zeros_(tensor)\n'
import torch
import numpy as np
import torch
input_data = np.array([[1, 2, 3], [4, 5, 6]])
tensor = torch.tensor(input_data)
torch.nn.init.zeros_(tensor)
print(tensor)