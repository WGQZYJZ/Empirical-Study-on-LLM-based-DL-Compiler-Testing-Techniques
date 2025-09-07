
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.softmax  = torch.nn.Softmax(dim=-1)
 
    def forward(self, q1, k1, v1, attn_mask=None):
        v2  = q1 @ k1.transpose(-2, -1)/math.sqrt(k1.size(-1))  # Compute the dot product of the query and key, and scale it
        v3  = v2 + attn_mask if (attn_mask is not None) else v2 
        v4  = self.softmax(v3)
        v5  = v4 @ v1  # Compute the dot product of the attention weights and the value
        return v5

# Initializing the model
m = Model()

# Inputs to the model
q1 = torch.randn(1, 20, 60)  # Initialize a query tensor with shape [batch size (N), sequence length (T), hidden dimension]
k1 = torch.randn(1, 34759, 8)  # Initialize a key tensor with shape [batch size (N), sequence length (T), hidden dimension]
v1 = torch.randn(1, 20, 60)  # Initialize another value tensor with shape [batch size (N), sequence length (T), hidden dimension]
attn_mask  = torch.zeros(1, k1.size(-2), k1.size(-1))  # Initialize an attention mask with the same shape as the key input

# Creating an instance of the model and running the forward pass
__output__  = m(q1, k1, v1)

