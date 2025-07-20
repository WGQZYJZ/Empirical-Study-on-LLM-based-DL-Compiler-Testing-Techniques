matrices = []
for i in range(5):
    matrices.append(torch.rand(5, 5))
result = torch.chain_matmul(*matrices)