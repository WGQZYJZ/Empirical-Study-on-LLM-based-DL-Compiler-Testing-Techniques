input_tensor = torch.randint(low=0, high=2, size=(4, 4), dtype=torch.int32)
other = torch.randint(low=0, high=2, size=(4, 4), dtype=torch.int32)
torch.Tensor.bitwise_right_shift_(input_tensor, other)