batch1 = torch.rand(5, 3, 4)
batch2 = torch.rand(5, 4, 6)
result = torch.Tensor.baddbmm(batch1, batch2, beta=1, alpha=1)