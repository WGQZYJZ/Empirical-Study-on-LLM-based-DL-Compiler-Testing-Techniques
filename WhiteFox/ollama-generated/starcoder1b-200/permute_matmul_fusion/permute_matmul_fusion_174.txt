
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = x1.permute(0, 2, 1)
        v2 = torch.bmm(v1, self.linear_weight)
        return v2


# Initializing the model
m = Model()


