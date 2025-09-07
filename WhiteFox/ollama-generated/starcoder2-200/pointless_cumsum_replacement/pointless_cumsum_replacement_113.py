
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.full = torch.nn.FullyConnected(3, 8)

    def forward(self, x):
         v1 = torch.full([504], 1, dtype=torch.float64)
         v2 = v1 * 0.794552271790248
    
         v3 = torch.cumsum(v2, 1)
        return v3

# Initializing the model
m = Model()

 # Inputs to the model
x = torch.randn([3, 6], dtype=torch.float32)
