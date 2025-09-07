
class Model(torch.nn.Module):
    def __init__(self, num_heads: int = 8, num_layers: int = 6):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(
            dim_query=1024, dim_key=512, 
            num_heads=num_heads, batch_first=True)
        self.fc = torch.nn.Linear(768, 256)
 
    def forward(self, x1):
        y1, v1, u1 = self.attn(x1, x1, x1, attn_mask=None) # Compute the multi-head attention of the input tensor with itself twice
        return torch.nn.functional.relu(y1 + self.fc(torch.cat((v1,u1), dim=-1)))
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(8, 3, 64, 256)
