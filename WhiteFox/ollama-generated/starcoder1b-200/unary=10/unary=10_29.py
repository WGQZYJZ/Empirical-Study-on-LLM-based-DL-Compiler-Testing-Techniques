
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2048, 10)

    def forward(self, x):
        v1  = x @ (x.t() / (torch.norm(x, dim=1).unsqueeze(-1))) # Multiply the input by the transpose of the input: `v1 * v1^T`
        v2 = v1 + 3 # Add 3 to the output of the previous step
        v3 = torch.clamp_min(v2, 0) # Clamp the output of the addition operation to a minimum of 0
        v4 = torch.clamp_max(v3, 6) # Clamp the output of the previous operation to a maximum of 6
        v5 = (v4 / 6) * 100 # Scale and shift the output from `0 ~ 6` so that we can do maths: `(v5 + 2)/400 * 100`
        return self.linear(v5)


# Initializing the model
m = Model()


