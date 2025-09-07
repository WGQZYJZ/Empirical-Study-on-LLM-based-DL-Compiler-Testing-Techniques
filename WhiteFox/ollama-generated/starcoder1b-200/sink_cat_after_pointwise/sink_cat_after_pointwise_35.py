
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        t1, t2 = torch.chunk(x1, 2, dim=-1) # Unpack a concatenated tensor
        return torch.cat([t1, t2], dim=0)


# Initializing the model
m = Model()


