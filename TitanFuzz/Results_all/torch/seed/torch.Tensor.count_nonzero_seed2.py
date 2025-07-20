_input_tensor = torch.randint(0, 2, (3, 4), dtype=torch.int32)
_output_tensor = torch.Tensor.count_nonzero(_input_tensor, dim=None)