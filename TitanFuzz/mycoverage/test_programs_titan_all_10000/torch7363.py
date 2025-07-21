import torch
from torch import nn
from torch.autograd import Variable
dependency_graph = [['torch', 'torchvision', 'torchaudio'], ['torch', 'torchvision', 'torchtext'], ['torch', 'torchvision', 'torchtext', 'torchaudio'], ['torch', 'torchvision', 'torchtext', 'torchaudio', 'torchsummary']]
try:
    torch.package.PackagingError(dependency_graph)
except Exception as e:
    print('Exception: ', e)