'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.conj_physical\ntorch.Tensor.conj_physical(_input_tensor)\n'
import torch
import numpy
_input_tensor = torch.randn(2, 3)
print('Input tensor: {}'.format(_input_tensor))
_conj_physical_tensor = _input_tensor.conj_physical()
print('Conjugate physical tensor: {}'.format(_conj_physical_tensor))
_numpy_tensor = _input_tensor.numpy()
_numpy_conj_physical_tensor = numpy.conj(_numpy_tensor).copy()
print('Numpy conjugate physical tensor: {}'.format(_numpy_conj_physical_tensor))