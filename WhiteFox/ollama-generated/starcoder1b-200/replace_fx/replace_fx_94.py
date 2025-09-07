
class Model(torch.nn.Module):
    def __init__(self, replace_fx):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)
        self.replace_fx = replace_fx

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional[self.replace_fx](v1)
        return v2


# Initializing the model
m = Model()


