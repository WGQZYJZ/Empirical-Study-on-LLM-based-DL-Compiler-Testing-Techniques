'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.inference_mode\ntorch.inference_mode(mode=True)\n'
import torch
input_data = torch.randn(1, 1, 224, 224)
torch.inference_mode(mode=True)
output_data = torch.randn(1, 1, 224, 224)
torch.inference_mode(mode=False)
print('input data: {}'.format(input_data))
print('output data: {}'.format(output_data))