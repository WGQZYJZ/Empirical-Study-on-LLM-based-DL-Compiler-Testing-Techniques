input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
shifts = torch.tensor([1, 2])
dims = torch.tensor([0, 1])
output_tensor = torch.Tensor.roll(input_tensor, shifts, dims)