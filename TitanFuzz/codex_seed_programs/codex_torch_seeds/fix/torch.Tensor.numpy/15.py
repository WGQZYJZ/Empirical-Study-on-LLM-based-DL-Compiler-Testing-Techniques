'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.numpy\ntorch.Tensor.numpy(_input_tensor)\n'
import torch
input_tensor_data = [1, 2, 3]
output_tensor_data = torch.Tensor.numpy(input_tensor_data)
print(output_tensor_data)