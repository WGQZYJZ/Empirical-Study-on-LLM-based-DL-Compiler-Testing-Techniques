
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key2):
        v3 = torch.matmul(query1, 0.5 * key2)
        return v3

# Initializing the model
m  = Model()

# Inputs to the model
k = torch.randn(16, 8)
k2 = torch.randn(4, 3, 4)

__output_2__  = m(torch.randn(3, 5), k * k2)

