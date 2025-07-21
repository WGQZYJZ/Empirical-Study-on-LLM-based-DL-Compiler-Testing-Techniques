import torch
from torch import nn

class ModelTanh(nn.Module):
    def forward(self, x):
        v = nn.Tanh()(x)
        return v[:, :, :, :]
m = Model()
# Inputs to the model
x = np.random.randn(*np.random.randint(0, 1000, size=(3, 75, 65)))
