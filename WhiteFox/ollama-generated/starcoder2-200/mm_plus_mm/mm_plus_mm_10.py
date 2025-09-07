
class Model(torch.nn.Module):
    def __init__(self, a1, b1, a2, b2):
        super().__init__()
        self.linear  = torch.nn.Linear(a1 * a2, b1 + b2)
 
    def forward(self, x1):
        v1  = torch.mm(x1[:, None], x1[None]) # Matrix multiplication between input and itself
        v3  = self.conv(v1).sum() # Sum of all the elements in the output from applying convolution to the matrix multiplication
        return v3


# Initializing the model
a1, a2 = random.randint(), random.randint()
a3, b3 = random.randint(), random.randint() 
b4, a4 = random.randint(), random.randint()
 
b1, b2 = torch.randint(0, 5, (random.randint())).sum().item(), torch.randint(0, 6, (random.randint())).sum().item() 
 
m = Model(a1 * a3, b1 + b3, a4, b4)


# Inputs to the model
x1  = torch.randn((25, random.choice([a1 * a3] * 5),random.choice([b3, a4] * 5),))


