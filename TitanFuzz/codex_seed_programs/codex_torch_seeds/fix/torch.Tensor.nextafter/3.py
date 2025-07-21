'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nextafter\ntorch.Tensor.nextafter(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0])
output_tensor = input_tensor.nextafter(other=1.0)
print(output_tensor)