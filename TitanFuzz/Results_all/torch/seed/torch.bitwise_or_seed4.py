input1 = torch.randint(0, 2, (3, 3), dtype=torch.int8)
input2 = torch.randint(0, 2, (3, 3), dtype=torch.int8)
output = torch.bitwise_or(input1, input2)