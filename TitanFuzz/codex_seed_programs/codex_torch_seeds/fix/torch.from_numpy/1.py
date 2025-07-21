'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.from_numpy\ntorch.from_numpy(ndarray)\n'
import torch
import numpy as np
input_data = np.array([[3, 1, 2], [1, 1, 1]])
torch_from_numpy = torch.from_numpy(input_data)
print(torch_from_numpy)
torch_tensor = torch.tensor(input_data)
print(torch_tensor)
torch_as_tensor = torch.as_tensor(input_data)
print(torch_as_tensor)
eye_tensor = torch.eye(2, 3)
print(eye_tensor)
zeros_tensor = torch.zeros(2, 3)
print(zeros_tensor)