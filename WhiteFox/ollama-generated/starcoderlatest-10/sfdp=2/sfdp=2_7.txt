
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key = torch.nn.Linear(512, 8)

    def forward(self, qk):
        v6 = torch.matmul(qk, self.key.weight) # The query is a matrix and the key is a vector, so you can multiply them. 
        return v6
# Initializing the model
m = Model()


# Inputs to the model
query  = torch.randn(8, 512, 64, 64)
key    = torch.randn(8, 3, 64, 64)
