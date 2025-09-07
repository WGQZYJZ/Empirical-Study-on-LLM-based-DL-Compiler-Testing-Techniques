
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 5)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other # Other tensor added to the output of the linear transformation
        v3 = F.relu(v2)
        return v3


# Initializing the model and the second tensor that is added to the output of the linear layer