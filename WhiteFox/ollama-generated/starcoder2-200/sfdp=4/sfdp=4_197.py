
class Transformer(nn.Module):
    def __init__(self, d_model=128, nhead=4):
        super().__init__()
 
        self._d  = d_model//nhead
 
        self.layers  = nn.Sequential(
            TransformerBlock(d_model),
            TransformerBlock(d_model)
        )
        self.linear  = nn.Linear(in_features=d_model, out_features=2*d_model)
 
    def forward(self):
        # Initialization
        q1  = torch.randn(size=(30456,))
        k1  = torch.randn(size=(768, 30456))
 
        # Computations
        k1  = k1 + 1e-9 * torch.eye(k1.shape[1], device=k1.device)
        v1  = torch.randint(low=-1000, high=1000, size=(768, ), dtype=torch.float32, device='cuda')
        mask  = torch.zeros((768,), dtype=torch.bool, device='cuda')
 
        # Attention
        v2  = self._scaled_dot_product_attention(q1, k1, v1, mask)

# Initialization of the model
m  = Model()

