'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_printoptions\ntorch.set_printoptions(precision=None, threshold=None, edgeitems=None, linewidth=None, profile=None, sci_mode=None)\n'
import torch
import numpy as np
input_data = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float32)
input_tensor = torch.from_numpy(input_data)
torch.set_printoptions(precision=4, threshold=2, edgeitems=2, linewidth=80, profile=None, sci_mode=None)
print(input_tensor)