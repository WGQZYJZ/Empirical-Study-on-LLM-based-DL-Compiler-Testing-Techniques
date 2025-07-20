_input_tensor = torch.randint(low=0, high=100, size=(1, 2, 3), dtype=torch.int16)
_output_tensor = torch.Tensor.is_signed(_input_tensor)