'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.q_zero_point\ntorch.Tensor.q_zero_point(_input_tensor)\n'
import torch
input_data = torch.randint(0, 256, (2, 3), dtype=torch.uint8)
print('Input data:')
print(input_data)
quantized_zero_point = input_data.q_zero_point()
print('Quantized zero point:')
print(quantized_zero_point)