
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.weight, bias=None)
        v2  = v1.permute(0, 2, 1) # v2 is permuted to (3, 5) tensor
        return v2


# Initializing the model
m = Model()
