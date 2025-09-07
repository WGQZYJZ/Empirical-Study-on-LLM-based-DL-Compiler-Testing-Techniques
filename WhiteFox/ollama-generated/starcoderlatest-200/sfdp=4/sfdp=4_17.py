
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(1, 8)
        self.key = torch.nn.Linear(1, 8)
 
    def forward(self, xq, xk):
        qk = torch.bmm(xq, xk.transpose(-2, -1)) / math.sqrt(xk.size(-1)) # Compute the dot product of the query and key, and scale it
        qk += attn_mask  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        output = attn_weight @ value  # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = Model()

# Inputs to the model
xq = torch.randn(2, 1, 64, 64)
xk = torch.randn(1, 8, 64, 64)
