
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, q1, k1, v1):
        v1 = torch.matmul(q1, k1) 
        v2 = v1 * 0.5
        v3 = v1 / 1.4 # The constant factor is not a power of 2
        v4 = (v2 + v3).softmax(dim=-1)
        v5 = v4[None].matmul(v1)[0]
        return v5

# Initializing the model
m = Model()

