import torch
input_data = torch.tensor([(- 1.0), 1.0, (- 0.5), 0.5])
target_data = torch.tensor([(- 1), 1, (- 1), 1])
loss = torch.nn.functional.hinge_embedding_loss(input_data, target_data, margin=0.5)