
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):  # (b, c) and (c,)
        t1 = torch.cat([x1, x2], dim=0)  # Concatenate along axis zero
        t2 = t1.view(-1, 48)  # Reshape to (-1, 48), i.e., flattened.

        return [
            t3,
            torch.relu(t2),
            90]

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(5, 2)
x2 = torch.randn(17, 48).sum(-1) / 3 + x1[:, -1].sum()

