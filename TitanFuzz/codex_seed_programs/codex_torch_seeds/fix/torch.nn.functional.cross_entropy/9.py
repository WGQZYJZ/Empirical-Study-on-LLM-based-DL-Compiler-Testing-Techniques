"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.cross_entropy\ntorch.nn.functional.cross_entropy(input, target, weight=None, size_average=None, ignore_index=-100, reduce=None, reduction='mean')\n"
import torch
from torch.autograd import Variable
import numpy as np
import torch
from torch.autograd import Variable
import numpy as np
batch_size = 5
num_classes = 2
num_inputs = 10
np.random.seed(42)
input = np.random.randn(batch_size, num_inputs)
target = np.random.randint(num_classes, size=(batch_size,))
input = torch.from_numpy(input).float()
target = torch.from_numpy(target).long()
output = torch.nn.functional.cross_entropy(input, target)
print(output)