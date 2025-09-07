
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        return torch.relu(x1.view(-1).mean())


# Initializing the model
m = Model()

# Inputs to the model
t1  = torch.randn([2], dtype=torch.float32)
