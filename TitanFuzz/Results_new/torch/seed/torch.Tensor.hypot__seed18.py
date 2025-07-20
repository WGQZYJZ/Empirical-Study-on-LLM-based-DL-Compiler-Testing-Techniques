input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.int32)
other = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.int32)
output_tensor = torch.Tensor.hypot_(input_tensor, other)