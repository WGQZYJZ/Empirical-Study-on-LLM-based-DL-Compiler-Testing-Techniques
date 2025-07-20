tensor1 = torch.rand(2, 3)
tensor2 = torch.rand(2, 3)
tensor3 = torch.rand(2, 3)
result = torch.block_diag(tensor1, tensor2, tensor3)