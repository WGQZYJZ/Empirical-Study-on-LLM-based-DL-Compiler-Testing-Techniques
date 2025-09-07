
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu = torch.nn.ReLU()

    def forward(self, t1, t2, ...):
        return self.relu(t1 + t2)  # Apply pointwise operation to tensors and then concatenate them with a dimension

# Inputs to the model
x1 = torch.randn(100, 3)
