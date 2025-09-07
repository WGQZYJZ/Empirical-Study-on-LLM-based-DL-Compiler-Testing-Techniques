
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = 16
        self.key = torch.randn(8, 32)
        self.value = torch.randn(8, 32)
 
    def forward(self, query):
        v1  = torch.nn.functional.normalize(query, p=2., dim=-1) 
        v2  = torch.matmul(v1, self.key.transpose(-2, -1)) / self.scale ** 0.5
        v3  = torch.nn.functional.softmax(v2, dim=-1)
        v4  = torch.nn.functional.dropout(v3, p=0.7, training=self.training) 
        v5  = v4 @ self.value
        return v5


# Initializing the model
m = Model()
 
# Inputs to the model
q1 = torch.randn(256, 8)
 
  