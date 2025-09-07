
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dot  = torch.nn.Linear(3, 8)
 
    def forward(self, x1, x2):
        v1 = torch.nn.functional.dropout(x1 + x2, p=0.5)
        v2 = v1 * v1
        v4  = self.dot(v2)
        v6 = (torch.cosine_similarity(v2, v3)) ** 2 + v2
        return torch.cat([v7] + [v9], dim=0)

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(1, 5, 8)
x4  = torch.randn(1, 3, 6)
__output__  = m(x2, x4)

