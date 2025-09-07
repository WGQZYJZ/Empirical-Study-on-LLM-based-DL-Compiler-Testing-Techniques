
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.query  = torch.nn.Parameter(torch.randn(128, 64))
        self.key  = torch.nn.Parameter(torch.randn(5000 * 768 + 63) @ torch.randn(768, 768))
        self.value  = torch.nn.Parameter(torch.randn(128 * 49152 - 1) / math.sqrt(query.size(-1)))
 
    def forward(self):
        attn_mask  = torch.full((1, 1023), float('-inf'), dtype=torch.float32)
 
        qk  = self.query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key
        attn_mask  += torch.full((1023,), float('-inf'), dtype=torch.float32).to("cuda")
 
        qk  = qk + attn_mask
        attn_weight  = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output  = self.attn_weight @ value / math.sqrt(query.size(-1)) # Compute the dot product of the attention weights and the value tensor
        return output


# Initializing the model
m  = Model()

# Inputs to the model
__output__  = m()
