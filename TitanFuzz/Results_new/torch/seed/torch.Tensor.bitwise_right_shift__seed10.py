input_tensor = torch.randint(low=0, high=10, size=(3, 3), dtype=torch.uint8)
output_tensor = torch.Tensor.bitwise_right_shift_(input_tensor, other=1)