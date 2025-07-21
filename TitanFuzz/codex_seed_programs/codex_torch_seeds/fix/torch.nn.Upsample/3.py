"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Upsample\ntorch.nn.Upsample(size=None, scale_factor=None, mode='nearest', align_corners=None)\n"
import torch
import torch
input_data = torch.randn(2, 3, 4, 4)
print('Input data:\n', input_data)
upsample = torch.nn.Upsample(size=(8, 8), mode='nearest')
output = upsample(input_data)
print('Output data:\n', output)
upsample = torch.nn.Upsample(size=(8, 8), mode='bilinear')
output = upsample(input_data)
print('Output data:\n', output)