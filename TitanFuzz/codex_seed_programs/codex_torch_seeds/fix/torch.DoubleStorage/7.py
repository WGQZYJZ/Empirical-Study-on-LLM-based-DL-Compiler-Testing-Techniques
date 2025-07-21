'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.DoubleStorage\ntorch.DoubleStorage(*args, **kwargs)\n'
import torch
input_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
double_storage = torch.DoubleStorage(input_data)
print(double_storage)