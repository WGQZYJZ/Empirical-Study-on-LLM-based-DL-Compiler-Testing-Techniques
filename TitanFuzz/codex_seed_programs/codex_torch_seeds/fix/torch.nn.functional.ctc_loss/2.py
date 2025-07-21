"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.ctc_loss\ntorch.nn.functional.ctc_loss(log_probs, targets, input_lengths, target_lengths, blank=0, reduction='mean', zero_infinity=False)\n"
import torch
import torch.nn.functional as F
import torch
(T, N, C) = (50, 32, 20)
S = 25
log_probs = torch.randn(T, N, C).log_softmax(2).detach().requires_grad_()
targets = torch.randint(1, C, (N, S), dtype=torch.long)
input_lengths = torch.full((N,), T, dtype=torch.long)
target_lengths = torch.randint((S // 2), S, (N,), dtype=torch.long)
loss = F.ctc_loss(log_probs, targets, input_lengths, target_lengths)