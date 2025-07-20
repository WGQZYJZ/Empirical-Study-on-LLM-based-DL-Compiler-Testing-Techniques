input_size = 4
hidden_size = 2
gru_cell = torch.nn.GRUCell(input_size, hidden_size)
input = torch.randn(6, 3, input_size)
hx = torch.randn(3, hidden_size)
output = []
for i in input:
    hx = gru_cell(i, hx)
    output.append(hx)