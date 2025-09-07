
class Model(torch.nn.Module):
    def __init__(self, config):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.fc = nn.Linear(config.vocab_size + config.hidden_dim * 2, config.vocab_size)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)  # Apply pointwise convolution with kernel size 1 to the input tensor
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        qk = (x2 * self.fc(v5)).unsqueeze(-1)  # Compute the dot product of the query and key, and scale it
        qk = qk / math.sqrt(x1.size(-1))  # Scale the result of the dot product
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        output = attn_weight @ v6  # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = Model(config=config)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
