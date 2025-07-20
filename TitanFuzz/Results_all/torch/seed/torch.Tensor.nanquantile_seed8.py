input_tensor = torch.tensor([[0.1, 0.2, 0.3, 0.4], [0.5, 0.6, 0.7, 0.8], [0.9, 1.0, 1.1, 1.2]])
result = torch.Tensor.nanquantile(input_tensor, 0.5, dim=None, keepdim=False)