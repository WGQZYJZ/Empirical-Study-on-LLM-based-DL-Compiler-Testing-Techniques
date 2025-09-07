
class MyTransformer(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, attn_mask=None):
        v1  = torch.einsum('bknh,lknm->blknm', [query, key]) / math.sqrt(key.shape[-1]) # Compute the dot product of the query and key tensors
        v2  = v1 + attn_mask  # Add the attention mask to the scaled dot product
        v3  = torch.softmax(v2, dim=-1)  # Apply softmax to the result
        return v3 @ value

# Initializing the model
model1 = MyTransformer()

# Inputs to the model
query1  = torch.randn(300,  768)
key1    = torch.randn(512, 300*768) # Key is longer than query!
value1  = torch.randn(512, 768) # Weights are smaller than the value!
print('Shapes', query1.shape, key1.shape, value1.shape)

 # Initialize the model with a larger tensor for the attention mask
attn_mask  = torch.randn(300, 512*768) > -np.inf
 
__output__  = model1(query1, key1, value1, attn_mask=attn_mask)

