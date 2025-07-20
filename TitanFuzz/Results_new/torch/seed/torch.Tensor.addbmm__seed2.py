batch1 = torch.randn(10, 3, 4)
batch2 = torch.randn(10, 4, 5)
result = torch.empty(10, 3, 5)
torch.Tensor.addbmm_(result, batch1, batch2, beta=1, alpha=1)