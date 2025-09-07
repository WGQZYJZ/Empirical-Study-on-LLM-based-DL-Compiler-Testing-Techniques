
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)  # The first element will be moved to the end of this reshaped tensor

        v2 = torch.cat([v1, v1], dim=1)  # This reshaped tensor can now be used as input for the linear function
        return torch.relu(v2.view(-1, self.linear.weight.shape[-1]))


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 2)
