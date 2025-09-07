
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_layer = torch.nn.MultiheadAttention(8, 12)
 
    def forward(self, x1, key, query):
        attn_mask  = torch.ones((x1.size(0), 8))
        qk  = self.attn_layer(x1, key, value=query, key_padding_mask=attn_mask)[0] # compute the dot product of the query and key, and scale it
        qk = qk + attn_mask # add the attention mask to the scaled dot product
        attn_weight  = torch.softmax(qk, dim=-1) # apply softmax to the result
        output = attn_weight @ value # compute the dot product of the attention weights and the value
        return output

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 8, 64, 64)
key = torch.randn(2, 12, 128, 50) # query and key are both 3-dimensional tensors
query = torch.randn(2, 12, 64, 50) # only value is 2-dimensional tensor
