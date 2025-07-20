_input_tensor = torch.randn(3, 3)
_dim = 0
_keepdim = False
_output_tensor = torch.Tensor.argmin(_input_tensor, dim=_dim, keepdim=_keepdim)