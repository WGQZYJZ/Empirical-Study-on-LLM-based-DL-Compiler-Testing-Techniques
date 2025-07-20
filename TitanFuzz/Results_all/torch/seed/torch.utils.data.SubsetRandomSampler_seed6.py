data = torch.randn(20, 3)
indices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sampler = torch.utils.data.SubsetRandomSampler(indices)
for i in sampler:
    print(i)