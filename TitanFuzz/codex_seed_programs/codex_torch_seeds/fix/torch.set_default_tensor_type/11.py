'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_default_tensor_type\ntorch.set_default_tensor_type(t)\n'
import torch
if True:
    print('PyTorch version:', torch.__version__)
    input_data = torch.rand(2, 3)
    print('Input data:', input_data)
    torch.set_default_tensor_type(torch.DoubleTensor)
    print('Tensor type:', input_data.type())