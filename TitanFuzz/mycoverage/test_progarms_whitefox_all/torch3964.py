import torch
from torch import nn

class Model(torch.nn.Module):
    def forward(self, model_input):
        intermediate = torch.add(model_input, model_input)
        intermediate = torch.add(intermediate, model_input)
        intermediate = torch.add(intermediate, model_input)
        intermediate = torch.add(intermediate, model_input)
        intermediate = torch.add(intermediate, model_input)
        return intermediate
m = Model()
# Inputs to the model
model_input = torch.randn(1, 3, 224, 224)
