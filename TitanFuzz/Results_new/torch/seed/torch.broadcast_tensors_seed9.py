tensor_a = torch.randn(1, 3)
tensor_b = torch.randn(3, 1)
tensor_c = torch.broadcast_tensors(tensor_a, tensor_b)