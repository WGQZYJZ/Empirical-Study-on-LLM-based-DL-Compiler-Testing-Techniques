'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.rnn.pad_packed_sequence\ntorch.nn.utils.rnn.pad_packed_sequence(sequence, batch_first=False, padding_value=0.0, total_length=None)\n'
import torch
import torch.nn as nn
import torch.nn.utils.rnn as rnn
input_data = torch.tensor([[1, 2, 3], [4, 5, 0], [6, 0, 0]])
input_lengths = torch.tensor([3, 2, 1])
(output_data, output_lengths) = rnn.pad_packed_sequence(rnn.pack_padded_sequence(input_data, input_lengths, batch_first=True), batch_first=True)
print(output_data)
print(output_lengths)