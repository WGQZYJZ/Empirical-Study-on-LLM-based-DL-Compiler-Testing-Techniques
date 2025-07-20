_input_tensor = torch.randn(3, 5)
_output_tensor = torch.Tensor.sort(_input_tensor, dim=(- 1), descending=False)