'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.chain_matmul\ntorch.chain_matmul(*matrices, out=None)\n'
import torch
import torch
input_data = torch.rand(10, 10)
output_data = torch.chain_matmul(input_data, input_data, input_data)
print(output_data)