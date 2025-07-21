'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ELU\ntorch.nn.ELU(alpha=1.0, inplace=False)\n'
import torch
input_data = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], dtype=torch.float32)
elu = torch.nn.ELU()
output_data = elu(input_data)
print(output_data)
elu2 = torch.nn.ELU(alpha=0.5)
output_data2 = elu2(input_data)
print(output_data2)