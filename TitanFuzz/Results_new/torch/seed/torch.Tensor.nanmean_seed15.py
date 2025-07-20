_input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
_output_tensor = torch.Tensor.nanmean(_input_tensor, dim=0, keepdim=False)