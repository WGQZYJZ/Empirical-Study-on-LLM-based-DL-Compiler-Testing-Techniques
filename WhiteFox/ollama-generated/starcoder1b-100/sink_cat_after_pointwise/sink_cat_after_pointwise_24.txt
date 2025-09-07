
class Model(torch.nn.Module):
    def __init__(self, num_inputs):
        super().__init__()
        self.linear = torch.nn.Linear(num_inputs, 2)

    def forward(self, x1):
        v1 = torch.cat([x1.view(x1.shape[0], -1), x1], dim=1)
        v2 = self.linear(v1)
        return v2


# Initializing the model
m = Model(num_inputs=4)


