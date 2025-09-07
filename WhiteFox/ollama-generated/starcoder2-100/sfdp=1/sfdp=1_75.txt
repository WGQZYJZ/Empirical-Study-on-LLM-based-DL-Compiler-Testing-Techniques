
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.query  = torch.randn(32, 64)
        self.key   = torch.randn(32, 1000)
        self.value = torch.randn(32, 1000)
 
        self.scale_factor = 1 / math.sqrt(self.query.size(-1))
        self.dropout_p    = 0.70
 
    def forward(self, input):
        v1  = torch.matmul(self.query, self.key.transpose(-2, -1))
        v2  = v1.div(self.scale_factor)
        v3  = v2.softmax(dim=-1)
 
        mask = (torch.ones_like(v3).triu_() + torch.zeros_like(v3)).bool()
        v4  = torch.nn.functional.dropout(v3, p=self.dropout_p, training=self.training)
 
        v5  = v4 @ self.value
        return v5


# Initializing the model