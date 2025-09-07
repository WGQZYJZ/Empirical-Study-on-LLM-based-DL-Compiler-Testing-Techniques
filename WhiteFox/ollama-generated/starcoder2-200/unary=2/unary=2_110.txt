
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(3, 8, kernel_size=1, stride=1)
 
    def forward(self, x1):
        v1  = self.convT(x1) 
        v2  = v1 * 0.5
        v3  = (v1 * v1)
        v4  = v3 * 0.044715
        v5  = v1 + v4
        v6  = v5 * 0.7978845608028654 
        v7  = torch.tanh(v6)
        v8  = v7 + 1  
        v9  = v2 * v8
        return v9

# Initializing the model with initial weights and a random input tensor
init_input = torch.randn(3, 5, 100, 100)
initial_model = Model().to(device='cpu')
initial_output = initial_model(x=init_input).detach()


