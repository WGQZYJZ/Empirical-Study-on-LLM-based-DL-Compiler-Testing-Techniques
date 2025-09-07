
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.dropout = torch.nn.Dropout(dropout_p)

    def forward(self, x1):
        # Compute the scaled dot product of the input and the embedding matrix, plus the attention mask
        qk = self.conv @ x1.transpose(-2, -1) / math.sqrt(x1.size(-1))
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = self.dropout(attn_weight, True)  # Apply dropout to the softmax output

        v = self.conv @ x1.transpose(-2, -1) / math.sqrt(x1.size(-1))
        out = attn_weight @ v  # Compute the dot product of the dropout output and the value

        return out


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
