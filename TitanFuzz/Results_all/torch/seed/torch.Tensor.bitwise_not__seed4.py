_input_tensor = torch.randint(0, 2, (2, 2), dtype=torch.uint8)
_output_tensor = torch.Tensor.bitwise_not_(_input_tensor)