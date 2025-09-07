
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query1, key1, attn_mask1, value1):

        qk  = torch.matmul(query1,key1.transpose(-2,-1))/math.sqrt(query1.size(-1))
        qk += attn_mask1 # Add the attention mask to the scaled dot product
        attn_weight = F.softmax(qk,dim=-1)  # Apply softmax to the result
        attn_weight = nn.Dropout(attn_p)(attn_weight) # Apply dropout to the softmax output
        output  = torch.matmul(attn_weight,value1) # Compute the dot product of the dropout output and the value

        return output

# Initializing the model
m = Model()

