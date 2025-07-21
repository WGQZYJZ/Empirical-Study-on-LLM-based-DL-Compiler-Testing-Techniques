"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.ctc_loss\ntorch.nn.functional.ctc_loss(log_probs, targets, input_lengths, target_lengths, blank=0, reduction='mean', zero_infinity=False)\n"
import torch
import torch.nn.functional as F
input_lengths = torch.tensor([5])
target_lengths = torch.tensor([3])
targets = torch.tensor([1, 2, 1])
log_probs = torch.tensor([[0.1, 0.6, 0.1, 0.1, 0.1], [0.1, 0.1, 0.6, 0.1, 0.1], [0.8, 0.1, 0.1, 0.1, 0.1], [0.6, 0.1, 0.1, 0.1, 0.2], [0.1, 0.1, 0.1, 0.1, 0.8]])
loss = F.ctc_loss(log_probs, targets, input_lengths, target_lengths)
print