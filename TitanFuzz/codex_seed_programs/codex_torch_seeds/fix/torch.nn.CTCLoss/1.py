"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.CTCLoss\ntorch.nn.CTCLoss(blank=0, reduction='mean', zero_infinity=False)\n"
import torch
import torch
log_probs = torch.FloatTensor([[[0.1, 0.6, 0.1, 0.1, 0.1], [0.1, 0.1, 0.6, 0.1, 0.1]], [[0.1, 0.1, 0.1, 0.6, 0.1], [0.6, 0.1, 0.1, 0.1, 0.1]]])
targets = torch.IntTensor([1, 2, 1, 2])
input_lengths = torch.IntTensor([2, 2])
target_lengths = torch.IntTensor([2, 2])
loss_fn = torch.nn.CTCLoss()
loss = loss_fn(log_probs, targets, input_lengths, target_lengths)
print(loss)