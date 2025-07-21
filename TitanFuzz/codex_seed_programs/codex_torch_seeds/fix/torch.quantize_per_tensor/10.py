'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.quantize_per_tensor\ntorch.quantize_per_tensor(input, scale, zero_point, dtype)\n'
import torch
input_data = torch.rand(2, 3)
quantized_data = torch.quantize_per_tensor(input_data, scale=1.0, zero_point=0, dtype=torch.quint8)
'\nTask 4: Print the input data\nTask 5: Print the quantized data\n'
print('Input data: ', input_data)
print('Quantized data: ', quantized_data)
'\nTask 6: Print the scale and zero_point of the quantized data\nTask 7: Print the data type of the quantized data\n'
print('Scale of quantized data: ', quantized_data.q_scale())