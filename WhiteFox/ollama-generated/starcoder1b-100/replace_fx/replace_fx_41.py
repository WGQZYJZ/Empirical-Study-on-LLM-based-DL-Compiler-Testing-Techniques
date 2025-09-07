
class Model(torch.nn.Module):
    def __init__(self, cfg=None):
        super().__init__()
        self.dropout  = torch.nn.functional.dropout(...)  # Replaces dropout with replacement node that will trigger the `gm.graph.erase_node` function below
        self.linear    = torch.nn.Linear(2, 2)
        self.dropout2  = torch.nn.functional.dropout(...)  # Replaces dropout with replacement node that will trigger the `gm.graph.erase_node` function below

    def forward(self, x1):
        v1 = self.dropout(x1)
        v2 = self.linear(v1)
        return v2


# Initializing the model
m = Model()

