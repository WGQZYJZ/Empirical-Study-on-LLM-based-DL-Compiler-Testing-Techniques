tensor1 = torch.randn(2, 3)
tensor2 = torch.randn(2, 1)
tensor_list = torch.broadcast_tensors(tensor1, tensor2)