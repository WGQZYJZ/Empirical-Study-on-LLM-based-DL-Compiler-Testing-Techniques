'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardswish\ntorch.nn.functional.hardswish(input, inplace=False)\n'
import torch
import numpy as np
if True:
    input_data = torch.tensor(np.array([[(- 1), (- 0.5), 0, 0.5, 1]]), dtype=torch.float)
    print('Input data: \n{}'.format(input_data))
    output_data = torch.nn.functional.hardswish(input_data, inplace=False)
    print('Output data: \n{}'.format(output_data))