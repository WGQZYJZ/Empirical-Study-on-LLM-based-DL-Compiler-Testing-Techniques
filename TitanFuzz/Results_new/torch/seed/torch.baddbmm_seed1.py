batch_size = 3
n = 4
m = 5
p = 6
input = torch.randn(batch_size, n, p)
batch1 = torch.randn(batch_size, n, m)
batch2 = torch.randn(batch_size, m, p)
output = torch.baddbmm(input, batch1, batch2)