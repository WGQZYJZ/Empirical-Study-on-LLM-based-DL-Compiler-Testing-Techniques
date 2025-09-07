
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        return torch.nn.functional.dropout(x1, p=0.5), torch.rand_like(x1, dtype=torch.float32)


# Initializing the model
m = Model()


