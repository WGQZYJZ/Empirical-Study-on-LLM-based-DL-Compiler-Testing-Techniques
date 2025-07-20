batch_size = 2
input_tensor = torch.randn(batch_size, 2, 3, 4, 5)
batch1 = torch.randn(batch_size, 2, 3, 4, 5)
batch2 = torch.randn(batch_size, 2, 3, 4, 5)
torch.Tensor.baddbmm_(input_tensor, batch1, batch2, beta=1, alpha=1)