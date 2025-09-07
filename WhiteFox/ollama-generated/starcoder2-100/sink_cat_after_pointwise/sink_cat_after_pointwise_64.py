
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1, input2):
        return torch.cat([input1, input2], 0).view(-1)

# Initializing the model