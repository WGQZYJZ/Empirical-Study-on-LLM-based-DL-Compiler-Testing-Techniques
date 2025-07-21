'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.exp_family.ExponentialFamily\ntorch.distributions.exp_family.ExponentialFamily(batch_shape=[], event_shape=[], validate_args=None)\n'
import torch
from torch.distributions.exp_family import ExponentialFamily
batch_shape = [2]
event_shape = [1]
exp_family = ExponentialFamily(batch_shape, event_shape)
print('The type of the object is: ', type(exp_family))
print('The batch shape is: ', exp_family.batch_shape)
print('The event shape is: ', exp_family.event_shape)