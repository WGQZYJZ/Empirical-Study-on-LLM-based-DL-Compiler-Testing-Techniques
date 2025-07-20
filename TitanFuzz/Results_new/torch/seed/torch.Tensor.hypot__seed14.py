input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
other = torch.tensor([[7, 8, 9], [10, 11, 12]], dtype=torch.float32)
result = torch.Tensor.hypot_(input_tensor, other)