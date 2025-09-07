

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v3 = torch.relu(x1)  # Sink the t1.view to this unary op
        return torch.sigmoid(v3), v3

# Initializing the model
m = Model()

