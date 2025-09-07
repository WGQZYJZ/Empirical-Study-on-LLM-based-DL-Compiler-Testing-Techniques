
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):

        # Inputs to the model
        query = torch.rand([4, 256])
        key = torch.rand([3890, 768])
        value = torch.rand([4, 256])
        attn_mask = torch.randint(low=1, high=3890, size=[4, 256]).float()

        qk = query @ key.transpose(-2,-1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key tensors
        qk += attn_mask # Add the attention mask to the scaled dot product

        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        
        output = attn_weight @ value  # Compute the dot product of the attention weights and the value tensor
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.rand(4,256)

__output__  = m(x1)
