
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, t1, t2):
        t3 = torch.cat([t1, t2], dim=2) # Sink cat op after pointwise op (i.e., no other tensor method is invoked afterwards).
        return torch.relu(t3)


# Initializing the model
m = Model()

