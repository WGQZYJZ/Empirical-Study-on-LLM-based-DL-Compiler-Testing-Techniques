
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.lowmem_dropout(v1, training=False)
        v3 = self.linear(v2)
        return v3

# Initializing the model
m = Model()

