
class Model(torch.nn.Module):
    def __init__(self, q_dim: int, k_dim: int):
        super().__init__()
        self.qkv = torch.nn.Linear(q_dim + k_dim, q_dim * 3)
 
    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=-1)
        w = torch.tanh(v1 @ self.qkv.weight)
        s = torch.softmax(w @ self.qkv.bias, -1)
        y = s @ self.qkv.weight.transpose(-2, -1).unsqueeze(-1)
        output = x1 + y
        return output


# Initializing the model
m = Model(q_dim=8, k_dim=32)

