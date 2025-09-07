
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Conv2d(3, 16, 7, stride=4, padding=0)
        self.key   = torch.nn.Conv2d(3, 16, 5, stride=2, padding=1)
 
    def forward(self, x):
        qk = self.query @ self.key.transpose(-2, -1) / math.sqrt(self.query.size(-1))
        qk = qk + torch.randn(qk.shape).to(x.device()) * 0.1 # Add a noise to the scaled dot product
        attn_weight = F.softmax(qk, dim=-1)
        attn_weight = F.dropout(attn_weight, dropout_p, True)
        output = attn_weight @ self.value
        return output


# Initializing the model
m = Model()

 # Inputs to the model
x  = torch.randn(4, 3, 16, 256, 256)
