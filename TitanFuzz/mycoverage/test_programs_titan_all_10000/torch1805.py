import torch
from torch import nn
from torch.autograd import Variable
if torch.distributed.is_torchelastic_launched():
    print('Torchelastic is launched')
input_data = torch.tensor([1.0, 2.0, 3.0, 4.0])