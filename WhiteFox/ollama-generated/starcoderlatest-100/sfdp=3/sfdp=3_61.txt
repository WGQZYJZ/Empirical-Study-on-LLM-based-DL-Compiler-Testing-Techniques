
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul = torch.nn.Linear(8 * 64, 12)
 
    def forward(self, qk):
        v1 = self.matmul(qk)
        return v1


# Initializing the model
m = Model()


# Inputs to the model
q1 = torch.randn(128, 32, 64, 16)
k1 = torch.randn(128, 32, 64, 16)
