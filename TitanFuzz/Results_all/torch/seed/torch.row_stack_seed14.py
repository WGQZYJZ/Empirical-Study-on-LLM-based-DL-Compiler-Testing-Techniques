input1 = torch.rand(3, 3)
input2 = torch.rand(3, 3)
input3 = torch.rand(3, 3)
output = torch.row_stack((input1, input2, input3))
output2 = torch.zeros(9, 3)
torch.row_stack((input1, input2, input3), out=output2)