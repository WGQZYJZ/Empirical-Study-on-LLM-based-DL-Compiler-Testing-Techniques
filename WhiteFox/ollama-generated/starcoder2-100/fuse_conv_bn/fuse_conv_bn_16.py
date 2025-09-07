
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t2 = torch.nn.functional.relu(x1) # 4
        return self.linear(t2), t2


# Initializing the model