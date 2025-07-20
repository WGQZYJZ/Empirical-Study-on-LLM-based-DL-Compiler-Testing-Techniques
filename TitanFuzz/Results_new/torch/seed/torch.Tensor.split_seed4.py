_input_tensor = torch.rand(10, 3, 2)
_split_tensors = torch.Tensor.split(_input_tensor, 2, dim=0)