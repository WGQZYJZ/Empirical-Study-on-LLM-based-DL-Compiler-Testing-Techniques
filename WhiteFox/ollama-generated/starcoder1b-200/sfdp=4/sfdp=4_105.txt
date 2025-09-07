
class Model(torch.nn.Module):
    def __init__(self, hidden_size=512):
        super().__init__()
        self.ln = torch.nn.LayerNorm(hidden_size)
        self.dropout = torch.nn.Dropout(0.4)
        self.w1  = torch.nn.Linear(hidden_size, 3 * hidden_size)
        self.w2  = torch.nn.Linear(3 * hidden_size, hidden_size)

    def forward(self, x1, x2):
        q = x1 @ x2.transpose(-2, -1)
        k = x2
        v = x2 @ x2.transpose(-2, -1)

        k += self.dropout(q / math.sqrt(k.size(-1)))  # Add dropout to prevent division by zero

        attn_weight = torch.softmax(k / math.sqrt(k.size(-1)), dim=-1)
        output = attn_weight @ v

        return self.ln(x1 + output), x2


# Initializing the model
m  = Model()
