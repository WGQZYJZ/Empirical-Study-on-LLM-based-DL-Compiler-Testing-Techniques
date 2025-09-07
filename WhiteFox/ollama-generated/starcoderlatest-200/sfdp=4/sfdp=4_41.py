
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key_projection = torch.nn.Linear(10, 20)
        self.query_projection = torch.nn.Linear(15, 25)
        self.value_projection = torch.nn.Linear(30, 40)
 
    def forward(self, x):
        q = self.key_projection(x).transpose(-2, -1)
        k = self.query_projection(x)
        v = self.value_projection(x)

        qk = torch.matmul(q, k)/math.sqrt(q.size(-1)) # Compute the dot product of the query and key, and scale it
        attn_weights = torch.softmax(qk + 1e-20, dim=-1) # Add the attention mask to the scaled dot product
        
        output = torch.matmul(attn_weights, v) # Compute the dot product of the attention weights and the value

        return output

# Initializing the model
m = Model()


