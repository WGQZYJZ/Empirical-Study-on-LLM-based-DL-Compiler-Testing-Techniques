
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1):
        return torch.relu((torch.cat([input2, input3], dim=0)).view(-1))


# Initializing the model