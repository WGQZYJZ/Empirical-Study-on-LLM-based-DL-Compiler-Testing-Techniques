
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3200, 10)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other_tensor # <- This is added to the result of the linear transformation
        v3 = F.relu(v2)        # <- ReLU activation function is applied on the output of the previous line
        return v3

# Initializing the model