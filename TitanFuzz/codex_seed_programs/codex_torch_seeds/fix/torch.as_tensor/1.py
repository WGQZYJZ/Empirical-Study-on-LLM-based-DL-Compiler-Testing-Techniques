'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.as_tensor\ntorch.as_tensor(data, dtype=None, device=None)\n'
import torch
input_data = [1, 2, 3]
tensor_data = torch.as_tensor(input_data)
print('The input data is: {}'.format(input_data))
print('The tensor data is: {}'.format(tensor_data))
numpy_data = np.array(input_data)
tensor_data = torch.from_numpy(numpy_data)
print('The tensor data is: {}'.format(tensor_data))
tensor_data = torch.ones(3)
print('The tensor data is: {}'.format(tensor_data))
tensor_data = torch.zeros(3)
print('The tensor data is: {}'.format(tensor_data))