import torch

input_data = torch.tensor([(- 1), (- 2), 3, 4, (- 5), (- 6), 7, 8], dtype=torch.float32)
abs_data = torch.abs(input_data)