
class Model(torch.nn.Module):
    def __init__(self, num_features):
        super().__init__()
        self.linear = torch.nn.Linear(num_features + 10, 20)
 
    def forward(self, x1, other):
        v1  = self.linear(torch.cat((x1, torch.tensor([[1]], requires_grad=False)), dim=-1))  # Add one more dimension for bias term in the linear layer
        v2 = v1 + other  # Multiply the output of the linear layer by other
        return v2


# Initializing the model
m = Model(num_features=8)
x1 = torch.randn(1, 3, 64, 64)
