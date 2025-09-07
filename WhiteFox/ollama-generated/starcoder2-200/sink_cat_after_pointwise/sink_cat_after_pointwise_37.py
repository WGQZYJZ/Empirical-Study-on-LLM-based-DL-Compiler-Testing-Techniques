
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v = torch.relu(x1)
        return 3 * v + v - torch.tanh(v)

 # Initializing the model