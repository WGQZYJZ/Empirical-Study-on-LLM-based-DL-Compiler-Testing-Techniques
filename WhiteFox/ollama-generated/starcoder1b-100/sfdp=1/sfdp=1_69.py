
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        qk   = torch.matmul(x1, x1.transpose(-2, -1))
        scale = torch.rsqrt(torch.mean(qk, dim=-1).unsqueeze(-1)) # Use rsqrt to avoid overflow error (e.g., `float('inf')` in pytorch).
        qk   = qk / torch.unsqueeze(scale, dim=-1)

        softmax_qk  = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        v   = dropout_qk.matmul(x2)  # Compute the dot product of the dropout output and the value tensor

        return v

# Initializing the model
m = Model()


