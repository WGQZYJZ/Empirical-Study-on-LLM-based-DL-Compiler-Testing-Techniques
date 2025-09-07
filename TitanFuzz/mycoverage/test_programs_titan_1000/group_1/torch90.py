import torch
from torch import nn
from torch.autograd import Variable
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
torch.package.Directory(root_dir, True)