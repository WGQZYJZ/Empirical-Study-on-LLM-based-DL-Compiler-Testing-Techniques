
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q = torch.nn.Linear(1024, 512)
        self.k = torch.nn.Linear(1024, 512)
 
    def forward(self, q, k):
        x_qk = torch.matmul(q, k.transpose(-2, -1))
        return x_qk
# Initializing the model
m = Model()


# Inputs to the model
q = torch.randn(1, 1024)
k = torch.randn(1, 1024)
