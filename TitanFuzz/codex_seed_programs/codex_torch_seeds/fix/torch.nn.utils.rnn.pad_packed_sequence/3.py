'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.rnn.pad_packed_sequence\ntorch.nn.utils.rnn.pad_packed_sequence(sequence, batch_first=False, padding_value=0.0, total_length=None)\n'
import torch
import torch.nn.utils.rnn as rnn
input_data = torch.randn(4, 3, 7)
input_data[1, 2, :] = 0
input_data[2, 1, :] = 0
input_data[3, 0, :] = 0
input_lengths = [3, 2, 2, 1]
packed_input = rnn.pack_padded_sequence(input_data, input_lengths, batch_first=True)
(unpacked_input, unpacked_lengths) = rnn.pad_packed_sequence(packed_input, batch_first=True)
print('Input data: \n', input_data)
print('Packed input: \n', packed_input)
print('Unpacked input: \n', unpacked_input)
print('Unpacked lengths: \n', unpacked_lengths)