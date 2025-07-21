'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.dequantize\ntorch.Tensor.dequantize(_input_tensor)\n'
import torch
import torch
input_tensor = torch.randint(low=0, high=255, size=(1, 3, 224, 224), dtype=torch.uint8)
output_tensor = torch.Tensor.dequantize(input_tensor)
print('The input tensor is:')
print(input_tensor)
print('The output tensor is:')
print(output_tensor)