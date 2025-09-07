
class Model(torch.nn.Module):
    def __init__(self, nin, num_out):
        super().__init__()
        self.linear = torch.nn.Linear(nin, num_out)

    def forward(self, x1):
        v1  = x1.permute(0, 2, 1)
        t1  = torch.cat([v1[:, :, i:i + 2] for i in range(0, v1.shape[1] - 2)], dim=-1)  # Split along the last dimension (channel).
        v2  = self.linear(t1)
        return v2


# Initializing the model
m = Model(nin=2, num_out=2)


# Inputs to the model
x1 = torch.randn(1, 2, 5)
