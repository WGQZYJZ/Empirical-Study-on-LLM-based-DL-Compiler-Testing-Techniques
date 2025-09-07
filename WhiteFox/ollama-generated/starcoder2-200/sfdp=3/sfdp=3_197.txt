
class AttentionModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Linear(32, 8)
        self.key   = torch.nn.Linear(32, 4)
 
    def forward(self, x1, scale_factor=0.57, dropout_p=0.9):
        v1  = self.query(x1).matmul(self.key(x1))
        v2  = v1.mul(scale_factor)
        v3  = torch.nn.functional.softmax(v2, dim=-1) 
        v4  = torch.nn.functional.dropout(v3, p=dropout_p, training=self.training)
        v5  = v4.matmul(torch.randn(8)) # Fake value tensor for demonstration purposes only
        return v5


# Initializing the model
m  = AttentionModel()


# Inputs to the model
x1 = torch.randn(2, 32)
 
