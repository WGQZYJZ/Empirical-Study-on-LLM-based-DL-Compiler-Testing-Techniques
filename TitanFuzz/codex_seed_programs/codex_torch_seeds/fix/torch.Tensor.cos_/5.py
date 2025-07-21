'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cos_\ntorch.Tensor.cos_(_input_tensor)\n'
import torch
import numpy as np
if True:
    print('PyTorch version:', torch.__version__)
    input_data = np.array([0, (np.pi / 4), (np.pi / 2), ((3 * np.pi) / 4), np.pi, ((5 * np.pi) / 4), ((3 * np.pi) / 2), ((7 * np.pi) / 4), (2 * np.pi)])
    print('Input data:', input_data)
    input_tensor = torch.tensor(input_data)
    print('Input tensor:', input_tensor)
    output_tensor = input_tensor.cos_()
    print('Output tensor:', output_tensor)
    expected_output = np.cos(input_data)
    print('Expected output:', expected_output)