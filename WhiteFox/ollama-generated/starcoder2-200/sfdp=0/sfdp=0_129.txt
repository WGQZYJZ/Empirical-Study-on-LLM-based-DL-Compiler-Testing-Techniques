
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1  = torch.matmul(x1, x2)
        v3  = v1 / np.sqrt(np.prod([v1.size(-2), v1.size(-1)]))
        v4  = v3.softmax(dim=-1)
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x1, x2 = torch.randn(20, 768), torch.randn(512, 768)

