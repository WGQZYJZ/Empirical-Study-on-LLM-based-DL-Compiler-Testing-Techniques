
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(768, 512)
        self.ln = nn.LayerNorm(512)
 
    def forward(self, x):
        attn = self.attn(x).tanh()
        attn = self.ln(attn)
        return output


# Initializing the model
m = Model()

