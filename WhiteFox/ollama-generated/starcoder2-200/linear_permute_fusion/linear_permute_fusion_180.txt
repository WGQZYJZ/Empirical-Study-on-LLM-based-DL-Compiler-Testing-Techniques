
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(4096, 512)

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear1.weight)
        v2 = v1.permute(-3,-2)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(5,784,64)
