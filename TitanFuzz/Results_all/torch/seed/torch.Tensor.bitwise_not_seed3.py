_input_tensor = torch.randint(low=0, high=2, size=(3, 3), dtype=torch.int8)
_output_tensor = torch.Tensor.bitwise_not(_input_tensor)