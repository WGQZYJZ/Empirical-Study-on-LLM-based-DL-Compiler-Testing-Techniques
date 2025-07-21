'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.zeros_\ntorch.nn.init.zeros_(tensor)\n'
import torch
from torch.autograd import Variable
tensor = torch.FloatTensor(3, 3)
torch.nn.init.zeros_(tensor)
print(tensor)