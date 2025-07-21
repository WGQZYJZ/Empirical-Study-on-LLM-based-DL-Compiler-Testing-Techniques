'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.promote_types\ntorch.promote_types(type1, type2)\n'
import torch
input_data = torch.rand(3, dtype=torch.float64)
input_data_int = torch.randint(10, (3,), dtype=torch.int32)
print(torch.promote_types(input_data.dtype, input_data_int.dtype))