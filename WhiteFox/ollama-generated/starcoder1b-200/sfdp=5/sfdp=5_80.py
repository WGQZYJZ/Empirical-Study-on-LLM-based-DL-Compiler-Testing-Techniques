
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2):
        attn_mask = (torch.eye(self.hidden_size, device='cuda') < 0.5).type(x1.dtype)
        qk  = x1 @ x2.transpose(-2, -1) / math.sqrt(x1.shape[-1])
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True)  # Apply dropout to the softmax output
        value = self.conv(x2).squeeze(-1) * attn_weight  # Compute the dot product of the dropout output and the value
        return value


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
