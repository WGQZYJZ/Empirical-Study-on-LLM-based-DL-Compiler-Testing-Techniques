
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, 0.5) # Drops out half of the inputs
        v2 = torch.rand_like(v1)                     # Generates a tensor with the same size as `v1` filled with random numbers
        return v1 + v2


# Initializing the model
m = Model()

