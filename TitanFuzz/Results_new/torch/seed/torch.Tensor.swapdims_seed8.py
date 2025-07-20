input_tensor = torch.rand(2, 3, 4)
swapdims_tensor = torch.Tensor.swapdims(input_tensor, 0, 2)