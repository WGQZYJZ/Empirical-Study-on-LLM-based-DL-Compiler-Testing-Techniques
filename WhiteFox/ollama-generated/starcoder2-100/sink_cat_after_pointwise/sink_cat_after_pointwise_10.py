
class Model(torch.nn.Module):
    def __init__(self, input1, input2):
        super().__init__()

        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1):
        v1 = torch.cat([x1], dim=0)
        v2 = v1.view(-1, 1).permute(0, 1, 4, 5, 3, 2).reshape(-1, 8)
        return self.linear(v2)


m = Model()

# Inputs to the model
x1 = torch.randn(2) # x1.shape: [N]
__output__  = m(x1)