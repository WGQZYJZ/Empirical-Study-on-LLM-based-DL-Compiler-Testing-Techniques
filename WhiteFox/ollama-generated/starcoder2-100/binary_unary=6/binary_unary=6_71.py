
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(20, 10)

    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 - other_param
        v3  = F.relu(v2)
        return v3


# Initializing the model