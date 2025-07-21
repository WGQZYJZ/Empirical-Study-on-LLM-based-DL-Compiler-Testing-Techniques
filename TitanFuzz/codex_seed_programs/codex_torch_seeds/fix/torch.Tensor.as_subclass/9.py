'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.as_subclass\ntorch.Tensor.as_subclass(_input_tensor, cls)\n'
import torch
input_tensor = torch.randn(4, 3)
sub_class_tensor = torch.Tensor.as_subclass(input_tensor, torch.FloatTensor)
print(sub_class_tensor)