
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        t1 = torch.cat((x1.squeeze(), v1.view(1, 4)), dim=1)
        v2 = torch.nn.functional.linear(t1, self.linear.weight, self.linear.bias)
        return v2


# Initializing the model
m = Model()


