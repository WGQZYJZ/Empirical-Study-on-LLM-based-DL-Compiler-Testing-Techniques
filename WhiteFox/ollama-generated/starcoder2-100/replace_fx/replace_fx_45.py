
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 10)

    def forward(self, x1):
        t1  = x1[0].permute(-1, -3)
        t2  = lowmem_dropout(t1, p=0.5)
        t3  = torch.rand_like(t1).to(t1) # .cuda()
        t4  = t2 * self.linear(x1[1])
        return [v for k, v in t4]


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(30, 5)
x2 = torch.rand_like(x1, device="cuda") # If the model is run on GPU.
__output__  = m([x1, x2])

