
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = [v1 + v1 + v1 for _ in range(len(v1))]  # A list with length equal to `len(input1)`
        return v2


# Initializing the model
m = Model()


