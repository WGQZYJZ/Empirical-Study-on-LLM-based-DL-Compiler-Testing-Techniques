
class Model(torch.nn.Module):
    def __init__(self, num_input):
        super().__init__()
        self.linear = torch.nn.Linear(num_input, 2)

    def forward(self, x1):
        # Reshape tensor before concatenation
        v1 = x1.view(-1, 2)

        # Relu: [B, N, 1] -> [B, N, 1]
        v2 = torch.relu(v1)

        # Linear: [B, N, 1] -> [B, N, 2]
        out = self.linear(v2)
        return out


# Inputs to the model
x1  = torch.randn(4, 5, 3)
