
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1, input2):
        v  = torch.cat([input1, input2], dim=3)
        v1 = torch.relu(v.view(-1, 4))
        return v1


# Initializing the model