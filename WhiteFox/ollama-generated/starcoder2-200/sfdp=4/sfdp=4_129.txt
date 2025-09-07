
class MyModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Parameter(torch.randn(128, 3))
 
    def forward(self, key):
        value = torch.ones(key.size())
        query = self.query 
        kq = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key tensor
        kq = kq + attn_mask  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(kq, dim=-1) 
        output = attn_weight @ value # Compute the weighted sum of the value tensor using the attention weights
        return value


# Initializing model instance
m = MyModel()

# Inputs for the model (key, attn_mask)
key  = torch.randn(32, 10, 8)
attn_mask  = torch.zeros(512, 768)

# Calling forward method of the model
__output__  = m(key)

