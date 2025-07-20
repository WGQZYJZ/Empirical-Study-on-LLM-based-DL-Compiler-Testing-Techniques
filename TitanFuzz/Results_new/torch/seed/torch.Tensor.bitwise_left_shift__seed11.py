input_tensor = torch.randint(low=0, high=2, size=(2, 2), dtype=torch.int8)
other = torch.randint(low=0, high=2, size=(2, 2), dtype=torch.int8)
output_tensor = torch.Tensor.bitwise_left_shift_(input_tensor, other)