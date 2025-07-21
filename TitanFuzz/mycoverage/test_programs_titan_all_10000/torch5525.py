import torch
from torch import nn
from torch.autograd import Variable
input_data = np.random.random(size=(2, 3, 4))
input_tensor = torch.from_numpy(input_data)
output_tensor = torch.nn.functional.silu(input_tensor)