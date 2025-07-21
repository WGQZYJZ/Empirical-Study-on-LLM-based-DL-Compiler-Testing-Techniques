import torch

input_data = torch.Tensor([[1, 2, 3], [4, 5, 6]])
other_data = torch.Tensor([[1, 1, 1], [1, 1, 1]])
output_data = torch.greater_equal(input_data, other_data)