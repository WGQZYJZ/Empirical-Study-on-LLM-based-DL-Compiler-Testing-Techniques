'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.log2_\ntorch.Tensor.log2_(_input_tensor)\n'
import torch
tensor = torch.randint(low=1, high=2, size=(2, 2), dtype=torch.float32)
torch.Tensor.log2_(tensor)
print(tensor)