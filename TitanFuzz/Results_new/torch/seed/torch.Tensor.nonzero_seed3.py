_input_tensor = torch.randint(low=0, high=9, size=(2, 3), dtype=torch.float32)
_nonzero_indices = torch.Tensor.nonzero(_input_tensor, as_tuple=False)