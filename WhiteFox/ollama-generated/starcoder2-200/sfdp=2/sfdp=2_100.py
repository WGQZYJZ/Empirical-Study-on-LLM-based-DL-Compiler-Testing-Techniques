
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.att = torch.nn.MultiheadAttention(embed_dim=768, num_heads=12)
 
    def forward(self, x1, x2):
        v1  = self.att(x1, None, None)[0]
        return v1


# Initializing the model
m  = Model()
 
 # Inputs to the model
x1 = torch.randn(567893, 768)
x2 = x1

 __output__  = m(x1, x2)

