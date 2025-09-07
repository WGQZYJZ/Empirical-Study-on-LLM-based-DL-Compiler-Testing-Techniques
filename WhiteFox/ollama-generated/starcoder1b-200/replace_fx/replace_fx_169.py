
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.functional.dropout  # Make a copy of dropout to keep the original node

    def forward(self, x1):
        return self.dropout(x1)


# Initializing the model
m = Model()


