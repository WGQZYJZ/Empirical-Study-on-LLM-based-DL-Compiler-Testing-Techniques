_input_tensor = torch.Tensor([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
_output_tensor = torch.Tensor.nanmean(_input_tensor, dim=0, keepdim=False)