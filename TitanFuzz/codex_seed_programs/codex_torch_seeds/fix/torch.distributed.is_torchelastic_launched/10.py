'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributed.is_torchelastic_launched\ntorch.distributed.is_torchelastic_launched()\n'
import torch
if torch.distributed.is_torchelastic_launched():
    print('Torchelastic is launched')
input_data = torch.tensor([1.0, 2.0, 3.0, 4.0])
print('Torchelastic is launched: ', torch.distributed.is_torchelastic_launched())