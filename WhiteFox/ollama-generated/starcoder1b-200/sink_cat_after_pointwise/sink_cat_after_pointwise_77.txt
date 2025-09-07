
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(...)

    def forward(self, x1):
        v1  = torch.cat([tensor1, tensor2], dim=...)
        v2 = v1.view(...)
        return ...


# Initializing the model
m = Model()


