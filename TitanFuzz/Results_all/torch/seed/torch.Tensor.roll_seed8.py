input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
shifts = [1, 2]
dims = [0, 1]
output_tensor = torch.Tensor.roll(input_tensor, shifts, dims)