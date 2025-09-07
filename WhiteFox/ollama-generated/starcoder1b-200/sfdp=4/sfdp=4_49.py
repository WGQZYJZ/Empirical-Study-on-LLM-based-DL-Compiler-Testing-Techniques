
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.fc   = torch.nn.Linear(64 * 8 * 8, 50)
 
    def forward(self, x1):
        qk = self.conv(x1) @ self.conv(x1).transpose(-2, -1) / math.sqrt(x1.size(-1))
        attn_weight = torch.softmax(qk, dim=-1)
        v = attn_weight @ x1  # Compute the weighted sum of the value tensor by multiplying with the output from the attention mechanism
        return self.fc(v)


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
