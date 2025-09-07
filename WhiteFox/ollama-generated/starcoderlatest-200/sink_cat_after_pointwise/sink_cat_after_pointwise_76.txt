
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.cat([x1, x1], dim=1)  # Sink the input tensor after a concatenation
        v2 = v1.view([-1])  # Reshape the sinked tensor
        v3 = torch.relu(v2)  # Apply ReLU to the reshaped tensor
        return self.linear(v3)


# Initializing the model
m = Model()


