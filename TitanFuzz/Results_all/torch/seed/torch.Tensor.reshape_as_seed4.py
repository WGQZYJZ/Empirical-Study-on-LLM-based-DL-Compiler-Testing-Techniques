input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
other_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
output_tensor = torch.Tensor.reshape_as(input_tensor, other_tensor)