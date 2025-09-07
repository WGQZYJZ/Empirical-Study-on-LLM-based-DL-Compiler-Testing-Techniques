
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scaled = 1000.0 / 384**2
        self.q = torch.nn.Parameter(
            torch.randn([96, 512], requires_grad=True)) # query
        self.k = torch.nn.Parameter(
            torch.randn([96, 512], requires_grad=True)) # key
        self.v = torch.nn.Parameter(
            torch.randn([384, 512], requires_grad=True)) # value
 
    def forward(self, x):
        v1 = torch.matmul(x, self.k.transpose(-2, -1)) / self.scaled 
        v2 = v1.softmax(dim=-1)
        v3 = v2.matmul(v3)
        return v4


# Initializing the model
m  = Model()


# Inputs to the model