_input_tensor = torch.randn(1, 3, 3)
_sorted_tensor = torch.Tensor.sort(_input_tensor, dim=(- 1), descending=False)