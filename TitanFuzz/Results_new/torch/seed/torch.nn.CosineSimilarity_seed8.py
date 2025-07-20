input1 = torch.rand(3, 4)
input2 = torch.rand(3, 4)
output = torch.nn.CosineSimilarity(dim=1, eps=1e-08)