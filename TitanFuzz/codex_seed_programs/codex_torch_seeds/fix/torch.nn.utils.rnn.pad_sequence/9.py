'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.rnn.pad_sequence\ntorch.nn.utils.rnn.pad_sequence(sequences, batch_first=False, padding_value=0.0)\n'
import torch
import torch
sequences = [torch.tensor([1, 2, 3]), torch.tensor([4, 5]), torch.tensor([6, 7, 8, 9])]
padded_sequences = torch.nn.utils.rnn.pad_sequence(sequences)
print(padded_sequences)
padded_sequences = torch.nn.utils.rnn.pad_sequence(sequences, batch_first=True)
print(padded_sequences)
padded_sequences = torch.nn.utils.rnn.pad_sequence(sequences, padding_value=1)
print(padded_sequences)