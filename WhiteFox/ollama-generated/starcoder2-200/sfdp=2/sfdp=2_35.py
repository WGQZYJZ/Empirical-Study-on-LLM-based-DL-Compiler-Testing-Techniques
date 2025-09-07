
class Attention(torch.nn.Module):
    def __init__(self, d_model=512, nhead=8,
                 dropout=0., bias=True, **kwargs):
        super().__init__()
        self.scale = math.sqrt(d_model)
 
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.norm  = torch.nn.LayerNorm()
 
    def forward(self, query):
        v1  = self.conv(query)
        v2  = self.norm(v1)
 
        return v2


# Initializing the model
model = Attention()
 
 # Inputs to the model
x1 = torch.randn(1,3,64,64)
 
__output__  = model(x1)
