
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q_proj = torch.nn.Linear(3, 2)
        self.k_proj = torch.nn.Linear(3, 2)
        self.v_proj = torch.nn.Linear(3, 1)
 
    def forward(self, x1):
        q = self.q_proj(x1)
        k = self.k_proj(x1)
        v = self.v_proj(x1)
        d_k = torch.sum(q * k, dim=-1, keepdim=True).expand(-1, -1, k.size(-1))  # Compute the dot product of the query and key tensor, and scale it
        dk = torch.div(d_k, math.sqrt(k.size(-1)))  # Compute the rescaling factor for the scaled dot product of the query and key tensors
        attn_weights = dk @ v
        return attn_weights


# Initializing the model
m = Model()

