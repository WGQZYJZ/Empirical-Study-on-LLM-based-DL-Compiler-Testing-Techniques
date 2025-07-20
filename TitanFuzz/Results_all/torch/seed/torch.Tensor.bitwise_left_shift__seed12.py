input_tensor = torch.randint(low=0, high=100, size=(3, 3), dtype=torch.int32)
other = torch.tensor(2)
output_tensor = torch.Tensor.bitwise_left_shift_(input_tensor, other)