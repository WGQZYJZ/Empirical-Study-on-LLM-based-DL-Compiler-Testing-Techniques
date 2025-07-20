batch1 = torch.rand(10, 3, 4)
batch2 = torch.rand(10, 4, 5)
result = torch.Tensor.baddbmm(batch1, batch2, beta=1, alpha=1)