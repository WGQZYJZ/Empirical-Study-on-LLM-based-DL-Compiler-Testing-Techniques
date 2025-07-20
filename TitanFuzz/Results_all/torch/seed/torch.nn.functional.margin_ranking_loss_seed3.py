input1 = torch.tensor([[1.0, 2.0, 3.0, 4.0]])
input2 = torch.tensor([[1.0, 2.0, 3.0, 4.0]])
target = torch.tensor([[1.0]])
output = torch.nn.functional.margin_ranking_loss(input1, input2, target)