_input_tensor = torch.randn(2, 3, 4)
_other_tensor = torch.randn(2, 3, 4)
torch.Tensor.type_as(_input_tensor, _other_tensor)