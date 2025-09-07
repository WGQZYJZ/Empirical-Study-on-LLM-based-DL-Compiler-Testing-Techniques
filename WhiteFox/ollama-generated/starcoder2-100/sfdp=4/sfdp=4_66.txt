
class Transformer(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        # Embedding layers
        self.embedding1 = torch.nn.Embedding(50, 768)
        self.pos_embeding = torch.nn.Parameter(torch.zeros(4, 2))
 
        # Transformer block
        self.block1 = torch.nn.TransformerEncoderLayer(d_model=768, nhead=3)
 
    def forward(self, input):
         
        query = input + self.pos_embeding.sum()
        key = input + self.pos_embeding.sum()
 
        # Compute the dot product of the query and key tensors, and scale it
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        # Add the attention mask to the scaled dot product
        attn_mask  = torch.triu(torch.ones(4, 4), diagonal=3).bool().unsqueeze(0).unsqueeze(1)
        qk = qk + attn_mask
 
        # Apply softmax to the result
        attn_weight = torch.softmax(qk, dim=-1)
 
        output = attn_weight @ value
        
        return output

# Initializing the model
m  = Transformer()
 
# Inputs to the model
input  = torch.randint(40, size=(28960,)) # 3 3x128x128 patches with each patch containing 512 channels
__output__  = m(input)

