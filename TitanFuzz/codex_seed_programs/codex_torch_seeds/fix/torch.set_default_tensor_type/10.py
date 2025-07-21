'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_default_tensor_type\ntorch.set_default_tensor_type(t)\n'
import torch
input_data = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
torch.set_default_tensor_type(torch.FloatTensor)
print('PyTorch version: ', torch.__version__)
print('input_data: ', input_data)
print('input_data type: ', input_data.dtype)