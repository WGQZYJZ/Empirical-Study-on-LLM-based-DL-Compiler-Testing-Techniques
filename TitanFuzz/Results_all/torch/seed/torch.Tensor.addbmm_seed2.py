batch1 = torch.randn(10, 3, 4)
batch2 = torch.randn(10, 4, 5)
result = torch.Tensor.addbmm(batch1, batch2, alpha=1, beta=1)