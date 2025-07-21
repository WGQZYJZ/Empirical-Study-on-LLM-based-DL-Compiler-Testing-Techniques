'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.rnn.pack_sequence\ntorch.nn.utils.rnn.pack_sequence(sequences, enforce_sorted=True)\n'
import torch
import torch
input_data = [torch.tensor([3, 10]), torch.tensor([1, 1]), torch.tensor([5])]
packed_sequence = torch.nn.utils.rnn.pack_sequence(input_data)
print('Packed sequence is: ')
print(packed_sequence)
print('Packed sequence data is: ')
print(packed_sequence.data)
print('Packed sequence batch_sizes is: ')
print(packed_sequence.batch_sizes)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.rnn.pad_packed_sequence\ntorch.nn.utils.rnn.pad_packed_sequence(sequence, batch_first=False, padding_value=0.0, total_length=None)\n'
import torch