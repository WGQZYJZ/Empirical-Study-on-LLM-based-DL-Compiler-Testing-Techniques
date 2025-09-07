
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.zeros_like(x1).permute(0, 2, 1)
        v2 = torch.nn.functional.conv2d(v1, self.linear.weight, stride=2, padding=2)
        return v2


# Initializing the model
m = Model()


