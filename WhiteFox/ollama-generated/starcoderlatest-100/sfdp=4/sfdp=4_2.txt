
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_q = torch.nn.Linear(768, 1024)
        self.linear_k = torch.nn.Linear(768, 1024)
        self.attn_scale = math.sqrt(512)

    def forward(self, q1):
        v = self.linear_q(q1) @ self.linear_k.transpose(-2, -1).float() / self.attn_scale
        attn_weight = torch.softmax(v, dim=-1)  # Apply softmax to the result
        output = attn_weight @ q1.transpose(-2, -1)
        return output


# Initializing the model
m = Model()
q1 = torch.randn(4, 768, 50, 50)


# Output of the model
