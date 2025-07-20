_input_tensor = torch.randint(low=0, high=2, size=(5, 5), dtype=torch.int)
_count_nonzero_tensor = torch.Tensor.count_nonzero(_input_tensor, dim=None)