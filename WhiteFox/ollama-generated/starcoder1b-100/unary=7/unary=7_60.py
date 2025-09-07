
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(in_features=4, out_features=5, bias=True)
        self.linear2 = torch.nn.Linear(in_features=5, out_features=3, bias=False)

    def forward(self, x):
        l1  = self.linear1(x)
        l2  = l1  * clamp(min=0, max=6, l1 + 3)
        l3  = l2 / 6
        return l3


# Initializing the model
m = Model()


