'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.to_mkldnn\ntorch.Tensor.to_mkldnn(_input_tensor)\n'
import torch
input_tensor = torch.rand(10, 10)
output_tensor = input_tensor.to_mkldnn()
print(output_tensor)