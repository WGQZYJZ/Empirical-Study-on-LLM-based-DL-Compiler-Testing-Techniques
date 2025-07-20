input_tensor = torch.tensor([0, 1, 0, 1], dtype=torch.uint8)
other = torch.tensor([0, 0, 1, 1], dtype=torch.uint8)
torch.Tensor.bitwise_or(input_tensor, other)