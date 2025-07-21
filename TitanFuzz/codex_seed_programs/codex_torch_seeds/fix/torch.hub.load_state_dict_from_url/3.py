'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hub.load_state_dict_from_url\ntorch.hub.load_state_dict_from_url(url, model_dir=None, map_location=None, progress=True, check_hash=False, file_name=None)\n'
import torch
from torch.autograd import Variable
import numpy as np
import torch
x_data = Variable(torch.Tensor([[1.0], [2.0], [3.0]]))
y_data = Variable(torch.Tensor([[2.0], [4.0], [6.0]]))
url = 'https://download.pytorch.org/models/resnet18-5c106cde.pth'
model = torch.hub.load_state_dict_from_url(url)
print(model)