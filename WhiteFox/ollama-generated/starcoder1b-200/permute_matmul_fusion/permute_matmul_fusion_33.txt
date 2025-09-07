
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.bmm = torch.nn.functional.bmm

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = self.bmm(v1, x2)
        return v2


# Initializing the model
m = Model()


