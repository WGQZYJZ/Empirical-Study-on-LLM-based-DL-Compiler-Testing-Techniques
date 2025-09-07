
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.dropout(v1, p=0.5, training=True) # Use the dropout optimization here to replace `torch.nn.functional.linear`
        return v2


# Initializing the model
m = Model()


