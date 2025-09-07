
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        x1_copy = x1.clone()
        x1_copy[..., 0] = x1[..., 1].permute(0, 2, 1)
        output  = self.linear(x1_copy)
        return output


# Initializing the model
m = Model()


