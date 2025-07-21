'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.negative\ntorch.negative(input, *, out=None)\n'
import torch
import torch
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
print('input_data: ', input_data)
output_data = torch.negative(input=input_data)
print('output_data: ', output_data)
output_data = torch.tensor([[0, 0, 0], [0, 0, 0]], dtype=torch.float32)
torch.negative(input=input_data, out=output_data)
print('output_data: ', output_data)