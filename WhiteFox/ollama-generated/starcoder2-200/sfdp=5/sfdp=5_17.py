
class Model(torch.nn.Module):
    def __init__(self, attn=128):
        super().__init__()
        self.linear = torch.nn.Linear(3*attn, 4)
 
    def forward(self, x):
        q  = x
        k = x 
        v  = x 
        attn_mask = torch.zeros((x.size(-2), x.size(-1)), dtype=torch.bool).to(x.device)
        for _ in range(attn):
            k = self.linear(k)
        k  = q @ k.transpose(-2, -1)/ math.sqrt(query.size(-1)) #Compute the dot product of the query and key, and scale it 
        k  = k + attn_mask # Add the attention mask to the scaled dot product
        attn_weight  = torch.softmax(k, dim=-1) # Apply softmax to the result
        attn_weight  = torch.dropout(attn_weight, dropout_p, True)# Apply dropout to the softmax output 
        output = attn_weight @ v # Compute the dot product of the dropout output and the value 
        return v 


# Initializing the model
m = Model()

