
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(768, 32)
        self.key   = torch.nn.Linear(768, 32)
        self.value = torch.nn.Linear(768, 32)
 
    def forward(self, x1):
        qk  = torch.einsum('bchw,bchw->bchwc', (x1, x1)) / math.sqrt(768) # Compute the dot product of the query and key, and scale it
        qk += attn_mask # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        output = torch.einsum('bchwc,bchw->bchw', (attn_weight, x1))  # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2048, 768) # The query tensor is a batch of sequences in the shape (2048, 768)
