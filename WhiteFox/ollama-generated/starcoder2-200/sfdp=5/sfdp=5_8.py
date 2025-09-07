
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.randn(20, 16)
        self.key = torch.randn(32, 8, 4) 
        self.value = torch.randn(32, 8, 4)
        self.attn_mask  = torch.randint(0, 257,(1, 4))
 
    def forward(self, x):
        vq = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        va = vq + attn_mask # Add the attention mask to the scaled dot product
        vw = torch.softmax(va, dim=-1)# Apply softmax to the result
        vd = vw  * self.dropout() # Apply dropout to the softmax output
        vo  = vd @ value # Compute the dot product of the dropout output and the value
        return vo


# Initializing the model
m  = Model()
 
# Input tensors to the model, with length equal to the size of the query (4) times the size of the key/value (16x8) each. In this case, this means that there are a total of 32 matrices of shape [4 x 16]
q = torch.randn(10 , 4 )
k = torch.randn(5, 16*8 )
 
# Initializing the dropout operation
p  = 0.5 
 
__output__  = m([q @ k], p)

