_input_tensor = torch.randn(3, 5)
_topk_tuple = torch.Tensor.topk(_input_tensor, 2, dim=1, largest=True, sorted=True)