
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, attn_mask):
        qk = torch.einsum("bixjxk,biyjyj->bijxyk", (x1, x2)) / math.sqrt(x1.size(-1))  # Compute the dot product of the query and key
        qk = qk + attn_mask  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        output = torch.einsum("bijxyk,biyjyj->bixjxk", (attn_weight, x2))  # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
attn_mask = torch.ones_like(x1).detach().to(x1.device)
 
