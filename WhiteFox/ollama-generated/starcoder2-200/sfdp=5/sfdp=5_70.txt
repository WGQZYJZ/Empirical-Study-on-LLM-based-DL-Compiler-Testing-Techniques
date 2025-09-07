
class Model(torch.nn.Module):
    def __init__(self, ):
        super().__init__()
 
    def forward(self, query, key, attn_mask, dropout_p=0.,  𝑣𝑎𝑙𝑢𝑒,  𝑘𝑒𝑦):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        qk = qk + attn_mask # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1)# Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True) # Apply dropout to the softmax output
        output  = attn_weight @ value# Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 640)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 64))


query = torch.randn(32, 960)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 1008)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 1008)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 900)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 800)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 800)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 800)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 800)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 800)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 800)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 800)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 800)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 800)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 800)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 800)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 800)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 800)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 800)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 800)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 800)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 800)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 800)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 800)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 800)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 800)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 800)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 800)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 800)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 800)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 800)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 800)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 800)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 800)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 800)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 800)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 800)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 800)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 800)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 800)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 800)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 800)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 800)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 800)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 800)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 800)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 800)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value = torch.randn(32, 768)
attn_mask = torch.zeros((1, 32, 49))


query = torch.randn(32, 800)# Initializing the model
m  = Model()
 

# Inputs to the model
key = torch.randn(32, 576)
value =