'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_warn_always\ntorch.set_warn_always(b)\n'
import torch
import numpy as np
input_data = np.random.randn(10, 3)
input_data_tensor = torch.tensor(input_data)
torch.set_warn_always(True)
print(input_data_tensor)