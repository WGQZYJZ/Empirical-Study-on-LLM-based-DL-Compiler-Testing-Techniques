
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.zeros([32], dtype=x1.dtype) + 0.5 
        v2  = torch.clamp_max(v1 + 64 * x1.pow(3), 89 - 71* x1.sqrt())
        v3  = (v2 * 0.05).sum()
        return v3

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn([32])
 
# Outputs of the model from the input data
y1  = m(x1)