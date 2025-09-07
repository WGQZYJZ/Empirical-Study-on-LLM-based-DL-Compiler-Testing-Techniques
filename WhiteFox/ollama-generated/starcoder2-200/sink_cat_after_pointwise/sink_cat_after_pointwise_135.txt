
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v0 = torch.cat([x1, x2], 1)
        v1 = v0.view(-1, x1.size()[0], 3).squeeze()
        v2 = torch.nn.functional.relu(v1)
        return v2

# Initializing the model<|end_of_model|>
m  = Model()

# Inputs to the model
x1 = torch.randn(3, 4)
x2 = torch.randn(600, 5)
__output__= m(x1, x2)

