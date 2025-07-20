_input_tensor = torch.tensor([1, 0, 0, 0, 1, 1, 0, 1], dtype=torch.uint8)
_output_tensor = torch.Tensor.bitwise_not(_input_tensor)