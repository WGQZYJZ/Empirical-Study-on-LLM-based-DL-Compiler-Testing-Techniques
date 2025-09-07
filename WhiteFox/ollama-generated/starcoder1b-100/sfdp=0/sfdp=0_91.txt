
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(3, 8)
        self.key = torch.nn.Linear(3, 8)
        self.value = torch.nn.Linear(8, 8)

    def forward(self, x1):
        query_weight = self.query(x1).unsqueeze(-2)
        key_weight   = self.key(x1).unsqueeze(0)

        return query_weight @ key_weight


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
