input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.uint8)
other = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.uint8)
torch.Tensor.bitwise_or(input_tensor, other)