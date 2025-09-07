
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(8, 4)
 
    def forward(self, query: Tensor, key: Tensor, value: Tensor) -> Tuple[Tensor]:
            attn_mask = torch.empty([])
            qk = query @ key.transpose(-2,-1)/math.sqrt(query.size(-1))
            qk = qk+attn_mask
            attn_weight = torch.softmax(qk, dim=-1) 
            output = attn_weight @ value
            return output

# Initializing the model<|end_of_model|>
m  = Model()

 # Inputs to the model<|end_of_inputs|>
query = torch.randn(640*25, 8)  
key   = torch.randn(640*25, 8)   
value = torch.randn(128*25, 32)   

 # Initializing the model<|end_of_inputs|>
output = m((query), (key), value)

