
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value): 
        v1  = torch.bmm(query, key)
        v2  = v1 / math.sqrt(float(key.size(-1)))
        v3  = v2 + attn_mask
        v4  = torch.softmax(v3, dim=-1)
        v5  = torch.bmm(v4, value)
        return v5


# Initializing the model
m  = Model()

# Inputs to the model
query = torch.randn(20, 32, 64).to(torch.float32)
key = torch.randn(20, 32, 64).to(torch.float32)
value = torch.randn(20, 16, 64).to(torch.float32)
 
# Creating an attention mask for the model
attn_mask  = torch.zeros([20, 32]).to(torch.int8) # Create a 2D array of zeros with size [20, 32] (for the number of query sequences and key-value pairs in the batch)
 
# Assigning values to the mask
attn_mask[1][5] =  1 
attn_mask[1][7] = 1
 
attn_mask  = torch.from_numpy(attn_mask).to(torch.bool) # Convert the array of zeros into a Boolean tensor
 
 
__output__  = m(query, key, value)
 
