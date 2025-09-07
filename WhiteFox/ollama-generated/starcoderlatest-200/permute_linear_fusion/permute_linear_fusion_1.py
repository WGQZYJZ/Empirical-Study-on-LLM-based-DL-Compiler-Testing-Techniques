
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1):
        v1 = torch.rand(3, 4, 2).permute(0, 2, 1)
        # Add additional permutations to make the tensor more complicated. 
        v2 = torch.cat((v1, v1, v1), dim=0)

        return v2


# Initializing the model
m = Model()
x1 = torch.randn(3, 4, 2)
