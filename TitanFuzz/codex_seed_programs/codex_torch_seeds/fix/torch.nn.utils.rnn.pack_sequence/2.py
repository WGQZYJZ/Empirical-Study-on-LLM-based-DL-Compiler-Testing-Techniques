'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.rnn.pack_sequence\ntorch.nn.utils.rnn.pack_sequence(sequences, enforce_sorted=True)\n'
import torch
x1 = torch.tensor([1, 2, 3])
x2 = torch.tensor([4, 5])
x3 = torch.tensor([6])
input_data = [x1, x2, x3]
packed_input_data = torch.nn.utils.rnn.pack_sequence(input_data)
print(packed_input_data)
print(packed_input_data.data)
print(packed_input_data.batch_sizes)
'\nTask 4: Call the API torch.nn.utils.rnn.pad_packed_sequence\ntorch.nn.utils.rnn.pad_packed_sequence(sequence, batch_first=False, padding_value=0.0, total_length=None)\n'