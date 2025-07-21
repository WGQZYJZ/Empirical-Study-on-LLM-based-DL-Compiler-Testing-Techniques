'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_default_tensor_type\ntorch.set_default_tensor_type(t)\n'
import torch
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
print('input_data = ', input_data)
torch.set_default_tensor_type(torch.FloatTensor)
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]])
print('input_data = ', input_data)