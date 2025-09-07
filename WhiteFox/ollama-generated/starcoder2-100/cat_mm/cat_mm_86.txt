
class Model(torch.nn.Module):
    def __init__(self, dim=20):
        super().__init__()

    def forward(self, x1):  # Assuming x1 is of shape (b, n), dim = 4
        v1  = torch.sum(x1) * torch.arange(dim)[None]
        v2  = v1 * self.weight
        return [v2 for i in range(5)]

m  = Model()
# Inputs to the model