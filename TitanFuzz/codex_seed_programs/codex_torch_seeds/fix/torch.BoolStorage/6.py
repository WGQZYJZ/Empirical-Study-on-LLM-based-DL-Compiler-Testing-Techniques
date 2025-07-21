'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.BoolStorage\ntorch.BoolStorage(*args, **kwargs)\n'
import torch
input_data = [True, False, True, True, False, True]
input_data = [True, False, True, True, False, True]
bool_storage = torch.BoolStorage(input_data)
print('bool_storage = ', bool_storage)
print('bool_storage[0] = ', bool_storage[0])