'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.from_numpy\ntorch.from_numpy(ndarray)\n'
import torch
import numpy as np
input_data = np.array([1, 2, 3])
tensor_data = torch.from_numpy(input_data)
print(tensor_data)
numpy_data = tensor_data.numpy()
print(numpy_data)
list_data = tensor_data.tolist()
print(list_data)
int_data = tensor_data.int()
print(int_data)
float_data = tensor_data.float()
print(float_data)
double_data = tensor_data.double()
print(double_data)