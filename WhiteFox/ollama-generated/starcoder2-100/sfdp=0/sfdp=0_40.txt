
class Attention(torch.nn.Module):
    def __init__(self, inv_scale: float = 1):
        super().__init__()
 
        self.key = torch.nn.Linear(32, 64)
        self.query = torch.nn.Linear(32, 64)
        self.value = torch.nn.Linear(32, 64)
 
    def forward(self, x):
        v1  = self.key(x).transpose(-2, -1) # (B,64,H,W)
        v2  = self.query(x) / inv_scale # (B, 32, H, W)
        v3  = torch.matmul(v2, v1) #  (B, 32, 50, 8)
        v4  = torch.softmax(v3, dim=-1) # (B,32,H,W)
        v6  = self.value(x) * v4.matmul(v1) #(B,32,50,8)
        return v6


# Initializing the model
m  = Attention()

# Inputs to the model
x = torch.randn(1, 32, 50, 8)
 
__output__  = m(x)

