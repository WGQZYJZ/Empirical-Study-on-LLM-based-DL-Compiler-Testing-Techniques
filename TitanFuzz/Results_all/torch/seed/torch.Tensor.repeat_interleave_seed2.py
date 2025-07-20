input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
output_tensor = torch.Tensor.repeat_interleave(input_tensor, repeats=2, dim=0)