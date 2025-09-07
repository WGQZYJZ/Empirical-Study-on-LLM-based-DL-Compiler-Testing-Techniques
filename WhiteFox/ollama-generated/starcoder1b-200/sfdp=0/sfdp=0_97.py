
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = torch.nn.Linear(48, 32)
        self.layer2 = torch.nn.Linear(32, 64)

    def forward(self, x):
        hidden_layer_1 = F.relu(self.layer1(x))
        hidden_layer_2 = F.relu(self.layer2(hidden_layer_1))
        return hidden_layer_2


# Initializing the model
m = Model()
# Inputs to the model
x  = torch.randn(1, 48)
