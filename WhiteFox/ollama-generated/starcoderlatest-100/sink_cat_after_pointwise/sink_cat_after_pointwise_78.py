
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 2)

    def forward(self, x1):
        v1 = torch.cat([x1, x1, x1], dim=0) # Concatenate along dimension 0
        v2 = v1.view(-1, 9) # Reshape to a tensor with shape (-1, 9)
        v3 = torch.relu(v2) # Apply ReLU to the resaped tensor and store the result in v4

        return self.linear(v3)


# Inputs to the model
x1 = torch.randn(10, 3)
