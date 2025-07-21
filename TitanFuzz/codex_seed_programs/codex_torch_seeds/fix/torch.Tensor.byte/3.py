'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.byte\ntorch.Tensor.byte(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
from torch.autograd import Variable
import numpy as np
from torch.utils.data import Dataset, DataLoader
import torch
from torch.autograd import Variable
import numpy as np
from torch.utils.data import Dataset, DataLoader
_input_tensor = np.random.rand(1, 2, 3, 4)
_input_tensor = torch.from_numpy(_input_tensor)
_input_tensor = Variable(_input_tensor)
_output_tensor = _input_tensor.byte()
print(_output_tensor)