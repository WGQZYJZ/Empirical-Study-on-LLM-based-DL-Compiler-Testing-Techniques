input = torch.randn(1, 3, 5, 5, 5)
norm = torch.nn.LazyInstanceNorm3d(3, affine=False)
output = norm(input)