
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.attn  = torch.nn.Linear(8, 8)
        self.dropout = torch.nn.Dropout(0.5)

    def forward(self, x1):
        qk   = x1 @ self.conv.weight / (math.sqrt(x1.size(-1)) + 1e-7)  # Compute the dot product of the query and key tensors, and scale it
        k    = x1  # Only the query weight is scaled to 1
        v    = self.dropout(x1 @ self.conv.weight / (math.sqrt(x1.size(-1)) + 1e-7))  # Compute the dot product of the value and key tensors, and scale it
        attn = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        return self.attn(attn @ v)


# Initializing the model
m  = Model()


