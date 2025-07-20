_input_tensor = torch.randint(10, (2, 3), dtype=torch.float32)
_output_tensor = torch.Tensor.absolute(_input_tensor)