
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.fc1   = torch.nn.Linear(8 * 64 * 64, 10)

    def forward(self, x1):
        # Pointwise convolution
        v1 = self.conv1(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476

        # Error function
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5

        # Scaled Dot-Product Attention layer
        scaled_dot_product = torch.matmul(v6, x1.transpose(-2, -1)) / (self.embedding_dim ** (-0.5))
        attention_weights = scaled_dot_product.softmax(dim=-1)
        
        # Value layer
        output = attention_weights.matmul(v6)

        return output


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
