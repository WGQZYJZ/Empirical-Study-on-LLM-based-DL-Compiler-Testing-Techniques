_input_tensor = torch.randint(low=0, high=10, size=(3, 3, 3), dtype=torch.int32)
_output_tensor = torch.Tensor.int_repr(_input_tensor)