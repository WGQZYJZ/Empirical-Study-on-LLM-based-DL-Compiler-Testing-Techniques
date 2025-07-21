import torch
from torch import nn
from torch.autograd import Variable
input_dim = 10
output_dim = 1
batch_size = 64
epochs = 10
model = nn.Linear(input_dim, output_dim)
optimizer = torch.optim.AdamW(model.parameters(), lr=0.001, betas=(0.9, 0.999), eps=1e-08, weight_decay=0.01, amsgrad=False)
for epoch in range(epochs):
    print('Epoch:', epoch)