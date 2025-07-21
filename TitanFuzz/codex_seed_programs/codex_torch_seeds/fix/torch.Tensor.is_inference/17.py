'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_inference\ntorch.Tensor.is_inference(_input_tensor)\n'
import torch
input_data = torch.randn(2, 3, dtype=torch.float)
output_data = torch.Tensor.is_inference(input_data)
print('Output data: ', output_data)