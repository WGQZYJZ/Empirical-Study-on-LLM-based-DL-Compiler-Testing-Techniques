'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.PairwiseDistance\ntorch.nn.PairwiseDistance(p=2.0, eps=1e-06, keepdim=False)\n'
import torch
import torch
input_data = torch.randn(2, 3)
print(input_data)
output_data = torch.nn.PairwiseDistance(p=2.0, eps=1e-06, keepdim=False)(input_data, input_data)
print(output_data)
input_data_1 = torch.randn(2, 3)
input_data_2 = torch.randn(2, 3)
output_data = torch.nn.PairwiseDistance(p=2.0, eps=1e-06, keepdim=False)(input_data_1, input_data_2)
print(output_data)