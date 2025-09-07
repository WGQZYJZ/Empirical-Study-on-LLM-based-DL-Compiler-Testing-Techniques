
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, attn_mask=None):
        v1 = torch.bmm(query / math.sqrt(query.size(-1)), key.transpose(-2, -1))  # Compute the dot product of the query and key
        if not attn_mask is None:
            v1 += attn_mask
        v2 = torch.softmax(v1, dim=-1) 
        return torch.bmm(v2, value)
 

# Initializing the model
m  = Model()

 # Inputs to the model
query = torch.randn(32, 50, 768)
key   = torch.randn(32, 50, 768)
attn_mask = torch.ones(32, 513, 50).type_as(query)

 # Initialize an attention mask that will prevent the model from attending to certain positions in the query tensor. In this example, the model will not attend to position `3`, and thus the value of attn_mask[0][2] will be set to zero
attn_mask[:, 3] = 0
 
 # Run the forward pass through the model with the initialized inputs
output = m(query, key)


