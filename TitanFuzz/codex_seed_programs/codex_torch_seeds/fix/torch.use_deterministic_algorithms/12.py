'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.use_deterministic_algorithms\ntorch.use_deterministic_algorithms(mode)\n'
import torch
input_data = torch.randn(10, 10)
torch.use_deterministic_algorithms(True)
output_data = torch.randn(10, 10)
print(output_data)