
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(8, 3)
        self.linear2 = torch.nn.Linear(3, 4)
 
    def forward(self, x1, x2):
        v1 = self.linear1(x1)
        v2 = self.linear2(v1)
        return v2


# Inputs to the model
q1 = torch.randn(64, 8) # query tensor (batch_size, dim)
k1 = torch.randn(32, 8) # key tensor (batch_size, num_heads * dim)
v1 = torch.randn(32, 3) # value tensor (batch_size, num_heads * dim)
