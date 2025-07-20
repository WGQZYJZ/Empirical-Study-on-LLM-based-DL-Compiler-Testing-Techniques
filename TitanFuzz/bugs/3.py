import torch
import numpy as np

torch.manual_seed(420)
torch.cuda.manual_seed_all(420)
x = torch.tensor([-0., 0., 0.])
y = torch.clamp(x, min=0, max=1)  # prints [-0., 0., 0.]
print(y)

x = x.cuda()
y = torch.clamp(x, min=0, max=1)  # prints [0., 0., 0.]
print(y)

x = np.array([-0., 0., 0.])
y = np.clip(x, 0, 1)
print(y)  # prints [0., 0., 0.]