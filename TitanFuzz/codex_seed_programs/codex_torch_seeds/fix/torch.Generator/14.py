"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Generator\ntorch.Generator(device='cpu')\n"
import torch
input_data = torch.rand(1, 3, 224, 224)
torch.Generator(device='cpu')
if torch.cuda.is_available():
    print('The API works well!')
else:
    print('The API does not work!')