
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, attn_mask=None):
        v1  = torch.bmm(query, torch.transpose(key,-2,-1)) / math.sqrt(query.size(-1)) #Compute the dot product of the query and key, and scale it
        if not attn_mask:
            v1 += 0
        else:
            v1 += attn_mask #Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(v1,dim=-2) # Apply softmax to the result
        v3  = key @ (torch.diag(attn_weight).unsqueeze(-2)) + value

# Initializing model
m  = Model()
 
# Input tensors for the model
query  = torch.randn(56 ,10, 48) #Query tensor of size [batch, query dimensionality, key length]
key = torch.randn(56 ,13, 48) #Key tensor of size [batch, key dimensionality, key length]
 
# Attention mask for the model
attn_mask  = torch.randn(query.size(-2),key.size(-2)) <0.5 #Attention mask that masks the lower diagonal entries of a matrix
 
