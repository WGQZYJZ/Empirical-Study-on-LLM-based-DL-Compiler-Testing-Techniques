_input_tensor = torch.rand(1, 2, 3, 4)
_output = torch.Tensor.storage_offset(_input_tensor)