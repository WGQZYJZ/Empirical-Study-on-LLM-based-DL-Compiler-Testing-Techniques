
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v = torch.split(x1, [320], 1) # Split the input tensor into two tensors of size (320,) along dimension 1
        return torch.cat([v[i] for i in range(len(v))], 1)

# Initializing the model
m = Model()
x1 = torch.rand(1, 640, 8, 9) # Input tensor of size (640, 8, 9)


