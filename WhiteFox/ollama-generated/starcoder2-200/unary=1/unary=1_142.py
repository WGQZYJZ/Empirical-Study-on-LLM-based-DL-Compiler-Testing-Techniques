
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 3)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 * 0.5
        v3  = (v1 ** 3 ) * 0.044715 
        v4  = v3  + v2
        v5  = torch.tanh(v4)
        v6  = v5  + 1
        v7  = v2  * v6
        return v7

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = np.random.randn(1, 1).astype(np.float32)
__output__  = m(torch.from_numpy(x1))

