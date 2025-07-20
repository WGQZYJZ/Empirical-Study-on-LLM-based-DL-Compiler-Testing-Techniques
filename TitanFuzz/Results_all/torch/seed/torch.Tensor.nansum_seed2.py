_input_tensor = torch.tensor([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
_output_tensor = torch.Tensor.nansum(_input_tensor, dim=None, keepdim=False, dtype=None)