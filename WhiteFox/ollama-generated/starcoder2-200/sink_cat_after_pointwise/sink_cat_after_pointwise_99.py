
class Model(torch.nn.Module):
    def __init__(self, x1):
        super().__init__()

        self.layer = torch.nn.Linear(2 * 30 + 50, 2)

    def forward(self, x1):

        v1 = torch.cat([x1], dim=1).permute(0, 2, 1)
        v2 = v1.view(-1, self.layer.in_features)
        v3 = self.layer(v2)
        return torch.relu(v3)

# Initializing the model with the input tensor x1 (with 50 channels). The 50 channel input should be reshaped to 450 after being concatenated, and then reshaped back to its original size after applying a pointwise unary operation like ReLU.
m = Model(x1)

