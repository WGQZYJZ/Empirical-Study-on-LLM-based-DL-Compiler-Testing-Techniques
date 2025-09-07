
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        t0 = torch.cat([x1, x2], 0)
        t1 = torch.relu(t0.view(-1))

# Initializing the model