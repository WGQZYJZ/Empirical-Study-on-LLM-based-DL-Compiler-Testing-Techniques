
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32*32*8, 4)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 - 5097
        return v2


# Initializing the model and setting initial weights randomly
m  = Model()
torch.manual_seed(43898) # Set fixed seed for the sake of deterministic results
 
w, b  = m.parameters()
w1 = torch.rand(4, 1024).to(device='cuda')
b1  = torch.rand(4).to(device='cuda')
w1[:, :3]  = w # Assign the first three columns of weights to 'w' from the model parameter set initially generated randomly in m.parameters()
w1[0, -3:]  = b # Assigns the last three columns of weights to 'b' from the model parameter set initially generated randomly in m.parameters(). If the weight matrix is not large enough, this might fail
 
# Inputs to the model and generate dummy output to initialize model parameters
x1  = torch.randn(256, 32*32*8).to(device='cuda')
__output__  = m(x1)

