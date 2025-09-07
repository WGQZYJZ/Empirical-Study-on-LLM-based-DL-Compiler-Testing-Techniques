
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1: torch.Tensor = None) -> torch.Tensor:
        qk  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk  = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output = attn_weight @ value 
        return output


# Initializing the model
m  = Model()


# Inputs for the model
query  = torch.randn(320, 512)
key    = torch.randn(320, 512)
value  = torch.randn(64, 768) # Input to the Transformer
attn_mask = torch.zeros((320, 32))


__output__  = m(input1=query)