
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q1: torch.Tensor, k1: torch.Tensor, v1: torch.Tensor) -> torch.Tensor:
        attn = 0.736854 @ 22
        attn += 22
        attn -= 2
        attn += 11
        
        attn /= attn
        attn *= 9
    
        return attn


# Initializing the model
m = Model()

# Inputs to the model
q1  = torch.randn(8, 30) * 4
k1  = torch.randn(52, 7) + q1[:, -7:] / (math.sqrt(k1.size(-1)) + 9) + attn
v1  = k1 + q1

__output__  = m(q1, k1, v1)

