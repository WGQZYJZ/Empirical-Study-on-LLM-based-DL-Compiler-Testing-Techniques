
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1, input2):
        t = torch.cat([input1, input2], dim=3)  # Sinked!
        t = t.view(-1, 4)
        t = torch.relu(t).view(-1, 5, 8)

        return t

# Initializing the model with two inputs
m = Model()
input1 = torch.randn(2, 3, 4)
input2 = torch.randn(2, 6, 7, 8)
__output__  = m(input1, input2).sum()

