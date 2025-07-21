import torch
input_data = torch.randint(low=0, high=10, size=(3, 2), dtype=torch.int)
result = torch.greater_equal(input_data, 5)