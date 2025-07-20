batch1 = torch.rand(4, 3, 2)
batch2 = torch.rand(4, 2, 3)
torch.Tensor.addbmm(batch1, batch1, batch2, beta=1, alpha=1)