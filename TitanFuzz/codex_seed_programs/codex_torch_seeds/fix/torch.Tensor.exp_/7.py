'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.exp_\ntorch.Tensor.exp_(_input_tensor)\n'
import torch
import numpy as np
data = np.array([(- 1), 0, 1])
tensor = torch.from_numpy(data)
print(tensor.exp_())