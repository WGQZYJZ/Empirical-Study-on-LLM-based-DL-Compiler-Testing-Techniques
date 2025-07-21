'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.erfinv\ntorch.Tensor.erfinv(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 3)
output_tensor = input_tensor.erfinv()
print('input_tensor: ', input_tensor)
print('output_tensor: ', output_tensor)
'\n# Results:\ninput_tensor:  tensor([[-0.6271,  0.9086,  0.7383],\n        [ 0.7133,  0.1110,  0.9078],\n        [-0.7710,  0.6405, -0.8479]])\noutput_tensor:  tensor([[-1.2320,  1.9496,  1.6129],\n        [ 1.5526,  0.1098,  1.9472],\n        [-1.8043,  1.3240, -1.9076]])\n'