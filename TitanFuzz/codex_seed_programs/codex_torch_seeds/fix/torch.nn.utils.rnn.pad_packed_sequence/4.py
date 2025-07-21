'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.rnn.pad_packed_sequence\ntorch.nn.utils.rnn.pad_packed_sequence(sequence, batch_first=False, padding_value=0.0, total_length=None)\n'
import torch
import torch
input_data = torch.randint(0, 10, (3, 5))
packed_sequence = torch.nn.utils.rnn.pack_padded_sequence(input_data, [5, 3, 2], batch_first=True)
pad_packed_sequence = torch.nn.utils.rnn.pad_packed_sequence(packed_sequence, batch_first=True)
print(pad_packed_sequence)