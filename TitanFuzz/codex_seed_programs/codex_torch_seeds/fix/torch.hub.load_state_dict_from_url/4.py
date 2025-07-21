'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hub.load_state_dict_from_url\ntorch.hub.load_state_dict_from_url(url, model_dir=None, map_location=None, progress=True, check_hash=False, file_name=None)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.autograd import Variable
import numpy as np
import torch
input_data = np.array([[3, 1], [1, 1], [1, 2], [2, 3]], dtype='float32')
input_data = Variable(torch.from_numpy(input_data))
url = 'https://s3.amazonaws.com/pytorch/models/resnet18-5c106cde.pth'
state_dict = torch.hub.load_state_dict_from_url(url)
print(state_dict.keys())