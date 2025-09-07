
class Model(torch.nn.Module):
    def __init__(self, ):
        super().__init__()
 
    def forward(self):
         qk  = query @ key.transpose(-2,-1)/math.sqrt(query.size(-1)) # compute the dot product of query and key
         qk=qk + attn_mask # add the attention mask to the scaled dot product 
         attn_weight=torch.softmax(qk,dim=-1)  #apply softmax to the result
         attn_weight=torch.dropout(attn_weight,dropout_p,True) # apply dropout to the softmax output
         output = attn_weight @ value  # compute the dot product of the dropout output and the value
         return output

# Initializing the model
m  = Model()

