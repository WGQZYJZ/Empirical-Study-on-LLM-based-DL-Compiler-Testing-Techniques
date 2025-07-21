'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.as_tensor\ntorch.as_tensor(data, dtype=None, device=None)\n'
import torch
a_list = [1, 2, 3]
a_numpy_array = np.array([1, 2, 3])
a_tensor = torch.tensor([1, 2, 3])
tensor_from_list = torch.as_tensor(a_list)
tensor_from_numpy = torch.as_tensor(a_numpy_array)
tensor_from_tensor = torch.as_tensor(a_tensor)
print(tensor_from_list)
print(tensor_from_numpy)
print(tensor_from_tensor)
print(tensor_from_list.dtype)
print(tensor_from_numpy.dtype)
print(tensor_from_tensor.dtype)
print(tensor_from_list.device)
print(tensor_from_numpy.device)
print(tensor_from_tensor.device)
print