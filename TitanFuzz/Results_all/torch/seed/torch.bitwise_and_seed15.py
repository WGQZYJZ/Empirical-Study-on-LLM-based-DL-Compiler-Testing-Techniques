input1 = torch.randint(low=0, high=2, size=(5, 5), dtype=torch.int32)
input2 = torch.randint(low=0, high=2, size=(5, 5), dtype=torch.int32)
output = torch.bitwise_and(input1, input2)