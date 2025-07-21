import torch
input_data = torch.arange(1, 11)
output_data = torch.logspace(start=1, end=10, steps=10)
output_data = torch.logspace(start=1, end=10, steps=10, base=2)