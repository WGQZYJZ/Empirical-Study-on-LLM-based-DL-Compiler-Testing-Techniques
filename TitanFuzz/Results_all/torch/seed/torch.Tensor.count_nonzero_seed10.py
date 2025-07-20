_input_tensor = torch.randint(low=0, high=2, size=(4, 4), dtype=torch.int32)
_output_tensor = torch.Tensor.count_nonzero(_input_tensor, dim=None)