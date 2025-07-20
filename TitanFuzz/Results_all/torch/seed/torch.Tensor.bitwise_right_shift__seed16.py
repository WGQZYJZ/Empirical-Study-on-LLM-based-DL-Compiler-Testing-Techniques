input_tensor = torch.randint(low=0, high=10, size=(2, 3), dtype=torch.int8)
output_tensor = torch.Tensor.bitwise_right_shift_(input_tensor, 1)