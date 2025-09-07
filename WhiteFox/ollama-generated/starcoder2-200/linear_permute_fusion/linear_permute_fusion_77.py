
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1  = torch.nn.functional.linear(x1, ...)
        v2  = v1.permute(...)
        return v2


# Initializing the model