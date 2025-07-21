'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ShortStorage\ntorch.ShortStorage(*args, **kwargs)\n'
import torch
input_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
input_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
output_data = torch.ShortStorage(input_data)
print('Type of output data: ', type(output_data))
print('Output data: ', output_data)
print('Size of output data: ', output_data.size())
print('Element of output data: ', output_data[0])
print('Element of output data: ', output_data[1])
print('Element of output data: ', output_data[2])
print('Element of output data: ', output_data[3])