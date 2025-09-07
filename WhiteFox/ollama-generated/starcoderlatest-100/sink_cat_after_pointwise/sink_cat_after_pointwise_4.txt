
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu = torch.nn.ReLU()

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=0)
        v2 = v1.view(-1, 4)
        v3 = torch.nn.functional.tanh(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 5) # batch_size=3, input_dim=5
x2 = torch.randn(6, 7) # batch_size=6, input_dim=7
