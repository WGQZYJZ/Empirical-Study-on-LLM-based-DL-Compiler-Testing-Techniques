batch_size = 10
input = torch.randn(batch_size, 10)
batch1 = torch.randn(batch_size, 10, 10)
batch2 = torch.randn(batch_size, 10, 10)
output = torch.baddbmm(input, batch1, batch2)