
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul = torch.nn.Linear(128, 512)
 
    def forward(self, qk):
        v1 = self.matmul(qk)
        return v1


# Initializing the model
m = Model()

# Inputs to the model
qk  = torch.randn(1024, 512, dtype=torch.float32).contiguous()
