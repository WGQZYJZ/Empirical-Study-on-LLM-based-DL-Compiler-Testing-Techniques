
class AttentionModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, mask=None) -> torch.Tensor:
 
        qk = (query @ key.transpose(-2,-1)) / math.sqrt(query.size(-1))
        if mask is not None:
            qk += mask
        qk = torch.softmax(qk, dim=-1)
        output  = qk@value
        return output

# Initializing the model
m  = AttentionModel()

 # Inputs to the model
 query = torch.rand(32, 64*50)
 key   = torch.rand(32, 64*17, 64*50)
 value = torch.rand(32, 64*17, 8)
 
 attn_mask = torch.full((32, 17), float('-inf'), device=query.device)
