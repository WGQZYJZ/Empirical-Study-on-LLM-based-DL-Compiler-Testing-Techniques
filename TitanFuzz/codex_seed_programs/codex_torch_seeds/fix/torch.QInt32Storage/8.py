'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.QInt32Storage\ntorch.QInt32Storage(*args, **kwargs)\n'
import torch
input_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
input_data_quantized_storage = torch.QInt32Storage(input_data)
print('input_data_quantized_storage = {}'.format(input_data_quantized_storage))