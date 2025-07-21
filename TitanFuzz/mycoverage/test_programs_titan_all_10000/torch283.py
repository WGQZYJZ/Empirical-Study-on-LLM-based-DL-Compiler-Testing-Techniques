import torch
from torch import nn
from torch.autograd import Variable
input_data = np.array([[(- 0.8273), 0.8135, 0.2638, (- 1.2944)], [(- 0.5337), 0.6918, 0.3177, (- 1.0743)], [(- 0.3896), 0.4865, 0.7547, (- 0.6152)]])
input_data = torch.tensor(input_data, dtype=torch.float32)
output = torch.nn.functional.gelu(input_data)