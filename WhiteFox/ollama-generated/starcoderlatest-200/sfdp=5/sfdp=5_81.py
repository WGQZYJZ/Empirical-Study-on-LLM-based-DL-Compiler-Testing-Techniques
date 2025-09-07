
class Model(torch.nn.Module):
    def __init__(self, q_dim, k_dim, v_dim):
        super().__init__()
        self.q = torch.nn.Linear(q_dim, k_dim)
        self.k = torch.nn.Linear(k_dim, k_dim)
        self.v = torch.nn.Linear(v_dim, k_dim)
 
    def forward(self, x1, x2):
        q  = self.q(x1).unsqueeze(-2) # B * nQ * H
        k  = self.k(x2).unsqueeze(-3) # B * nK * W
        v  = self.v(x2) # B * nV * W
        x1 = q @ k.transpose(-2, -1) / math.sqrt(q.size(-1)) # B * nQ * W * H
        attn_weight  = torch.softmax(x1, dim=-1) # Apply softmax to the result
        output  = attn_weight  @ v # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = Model(q_dim=3, k_dim=8, v_dim=64)


# Inputs to the model
x1 = torch.randn(1, 32) # B * nQ
x2 = torch.randn(1, 32) # B * nK
