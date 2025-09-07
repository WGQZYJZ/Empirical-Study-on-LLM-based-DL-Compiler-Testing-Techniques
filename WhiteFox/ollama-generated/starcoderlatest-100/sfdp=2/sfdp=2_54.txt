
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(
            embed_dim=512, num_heads=8)
 
    def forward(self, qk1, v1):
        output  = self.attention(qk1, kq=v1, value=v1)[0] # Apply multi-head attention to the query and key tensors. 
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(8, 3, 512)
