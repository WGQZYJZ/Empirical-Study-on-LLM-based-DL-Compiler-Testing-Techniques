
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(1, 3)
        self.key = torch.nn.Linear(2, 3)
        self.value = torch.nn.Linear(4, 5)
 
    def forward(self, x):
        qk = (x @ self.key.weight.t()) / math.sqrt(self.query.weight.size(-1)) # Compute the dot product of the query and key, and scale it
        attn_mask = torch.unsqueeze(torch.unsqueeze(attn_mask, -2), -3)  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk + attn_mask, dim=-1) # Apply softmax to the result
        output = self.value(attn_weight) @ self.key.weight.t() # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = Model()

# Inputs to the model
attn_mask = torch.randn((2, 3, 4, 5))
