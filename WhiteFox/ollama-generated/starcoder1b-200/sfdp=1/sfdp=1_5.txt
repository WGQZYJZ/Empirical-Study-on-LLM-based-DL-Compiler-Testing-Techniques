
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(3072, 1)

    def forward(self, x1, x2):
        query = torch.tanh(self.attn(x1))
        key    = torch.tanh(self.attn(x2))
        value  = torch.tanh(self.attn(x2))
        return query * key


# Initializing the model
m = Model()

