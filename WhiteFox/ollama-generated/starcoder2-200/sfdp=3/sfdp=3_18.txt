
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk  = torch.nn.Linear(128, 36)
 
    def forward(self, q1, k1):
        v1  = self.qk(q1)
        v2  = v1 * scale_factor 
        v3  = torch.softmax(v2, -1)
        v4  = torch.nn.functional.dropout(v3, p=p)
        v5  = v4 @ k1
        return v5

# Initializing the model
m  = Model()

# Inputs to the model
q1  = torch.randn(8, 2048)
k1  = torch.randn(64, 399, 2048)
__output__  = m(q1, k1)

