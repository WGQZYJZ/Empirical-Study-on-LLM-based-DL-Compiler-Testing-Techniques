
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2):
        qk = x1 @ x2.transpose(-2, -1) / math.sqrt(x1.size(-1))
        attn_mask = (1.0 + 0.9 * torch.randn(x1.size()).bernoulli())

        # Compute the dot product of the query and key, and scale it
        qk = qk + attn_mask
        attn_weight = nn.Softmax(dim=-1)(qk)

        # Apply dropout to the softmax output
        attn_weight = nn.Dropout(dropout_p)(attn_weight)

        value = self.conv(x2)  # Compute the dot product of the dropout output and the value

        # Compute the dot product of the value and the attention weights
        # and scale it
        output = attn_weight @ value
        return output


# Initializing the model
m = Model()


