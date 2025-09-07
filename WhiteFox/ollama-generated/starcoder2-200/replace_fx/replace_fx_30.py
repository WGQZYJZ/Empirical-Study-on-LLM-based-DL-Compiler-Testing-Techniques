
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2 = torch.rand_like(x1).type_as(x1)
        v3 = 1 - torch.nn.functional.dropout(v2, p=0.5, training=True)

        # ...
        return v3

# Initializing the model
m = Model()

