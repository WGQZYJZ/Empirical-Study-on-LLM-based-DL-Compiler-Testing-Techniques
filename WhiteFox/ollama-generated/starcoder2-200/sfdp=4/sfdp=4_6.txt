
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        attn_mask = None
 
        qk  = torch.matmul(query, torch.transpose(key, -2,-1)) / math.sqrt(query.size(-1))
        if not self.__class__.attn_mask == None:
            attn_mask += self.__class__.attn_mask # Add the attention mask to the scaled dot product
 
        attn_weight  = torch.softmax(qk, dim=-1)
        output = torch.matmul(attn_weight , value)
        return output


# Initializing the model with parameters
Model.attn_mask = torch.ones((2048, 2048), dtype=torch.bool) # Setting the attention mask to a dummy tensor. Feel free to use your own attention mask here.
m  = Model()

# Inputs to the model