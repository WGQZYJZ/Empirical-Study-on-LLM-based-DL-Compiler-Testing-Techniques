input_size = 3
hidden_size = 5
gru_cell = torch.nn.GRUCell(input_size, hidden_size)
for param in gru_cell.parameters():
    print(param)
input = torch.randn(4, 3)
hx = torch.randn(4, 5)
output = gru_cell(input, hx)