
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key1, value1, attn_mask):
        v1 = torch.matmul(query1, key1.transpose(-2, -1)) / math.sqrt(query1.size(-1)) # Compute the dot product of the query and key, and scale it
        v1 += attn_mask  # Add the attention mask to the scaled dot product
        v3 = torch.softmax(v1, dim=-1)  # Apply softmax to the result
        v5 = torch.matmul(v3, value1)  # Compute the dot product of the attention weights and the value
        return v5


# Initializing the model
m  = Model()


# Inputs to the model
query1 = torch.randn(2,8 , 64 )
key1 = torch.randn(2,8, 37)
value1 = torch.randn(2,37,32)
attn_mask = torch.ones(size=(8,37))

 __output__= m(query1, key1 , value1, attn_mask)

# The output tensor contains the attention weights. We expect to see that they add up to 1 within each row and have a mean of around 0.5


