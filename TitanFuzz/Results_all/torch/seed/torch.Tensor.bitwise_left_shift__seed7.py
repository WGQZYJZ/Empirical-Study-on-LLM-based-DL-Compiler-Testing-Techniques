input_tensor = torch.rand(4, 4)
other = torch.ones(4, 4)
torch.Tensor.bitwise_left_shift_(input_tensor, other)