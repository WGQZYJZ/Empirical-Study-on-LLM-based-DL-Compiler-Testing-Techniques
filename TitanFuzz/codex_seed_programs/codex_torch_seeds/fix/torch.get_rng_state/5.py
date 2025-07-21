'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.get_rng_state\ntorch.get_rng_state()\n'
import torch
import numpy as np
data = np.random.rand(2, 3)
torch.get_rng_state()
'\nTask 4: Call the API torch.set_rng_state\ntorch.set_rng_state(state)\n'
torch.set_rng_state(torch.get_rng_state())
'\nTask 5: Call the API torch.manual_seed\n'
'\nTask 6: Call the API torch.cuda.manual_seed\ntorch.cuda.manual_seed(seed)\n'
torch.cuda.manual_seed