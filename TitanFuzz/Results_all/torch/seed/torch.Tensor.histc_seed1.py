_input_tensor = torch.rand(100)
_output_tensor = torch.Tensor.histc(_input_tensor, bins=100, min=0, max=0)