'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.rnn.pad_packed_sequence\ntorch.nn.utils.rnn.pad_packed_sequence(sequence, batch_first=False, padding_value=0.0, total_length=None)\n'
import torch
import torch.nn as nn
import torch
batch_size = 3
sequence_length = 4
input_size = 5
input = torch.randn(batch_size, sequence_length, input_size)
packed_input = nn.utils.rnn.pack_padded_sequence(input, [sequence_length, (sequence_length - 1), (sequence_length - 2)], batch_first=True)
print(packed_input)
(unpacked_input, unpacked_lengths) = nn.utils.rnn.pad_packed_sequence(packed_input, batch_first=True)
print(unpacked_input)
print(unpacked_lengths)