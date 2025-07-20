x1 = torch.tensor([1, 2, 3])
x2 = torch.tensor([4, 5])
x3 = torch.tensor([6])
input_data = [x1, x2, x3]
packed_input_data = torch.nn.utils.rnn.pack_sequence(input_data)