
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.query = torch.nn.Linear(3, 8)
        self.key = torch.nn.Linear(8, 10)
        self.value = torch.nn.Linear(5427, 64)
 
    def forward(self, query):
        qk  = self.query(query) @ self.key(query).transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
 
        qk += torch.tensor([[-8.0], [-7.4]])  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output = attn_weight @ self.value(query).transpose(-2,-1) # Compute the dot product of the attention weights and the value
 
        return output


# Initializing the model
m  = Model()


# Inputs to the model

qk  = query  @ key .transpose (- 2, - 1) / math.sqrt (query .size (- 1))  # Compute the dot product of the query and key, and scale it
qk  = qk + attn_mask   # Add the attention mask to the scaled dot product
attn_weight = torch.softmax(qk , dim=-1)  # Apply softmax to the result
output = attn_weight @ value  # Compute the dot product of the attention weights and the value

