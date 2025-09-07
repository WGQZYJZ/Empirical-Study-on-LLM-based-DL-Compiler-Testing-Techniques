
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query: Tensor, key: Tensor, value: Tensor, attn_mask: Tensor = None) -> Tensor:
        qk  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key tensors
        if attn_mask is not None:
            qk += attn_mask # Add the attention mask to the scaled dot product
        attn_weight  = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output  = attn_weight @ value # Compute the dot product of the attention weights and the value tensor
        return output


# Initializing the model
m  = Model()


# Inputs to the model
query   = torch.randn(2,8)
key     = torch.randn(320,8,640)
value   = torch.randn(1024,512)
attn_mask    = torch.zeros((2, 1))


# Initializing an example model instance
m.__init__()
 
 
