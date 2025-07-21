'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_default_tensor_type\ntorch.set_default_tensor_type(t)\n'
import torch
import numpy as np
input_data = np.array([[3, 2.5], [1, (- 1)], [(- 1), (- 1.5)], [(- 3), (- 2)]])
torch.set_default_tensor_type(torch.FloatTensor)
tensor_data = torch.from_numpy(input_data)
print('Task 4: Convert input data to tensor: \n{}'.format(tensor_data))