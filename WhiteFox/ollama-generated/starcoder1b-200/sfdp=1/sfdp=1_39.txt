
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = torch.nn.Linear(3, 64)
        self.layer2 = torch.nn.Linear(64, 64)
 
    def forward(self, x):
        v1 = self.layer1(x)
        v2 = self.layer2(v1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
k_q = torch.randn(3, 4)
k_q_t = k_q.transpose(-2, -1) # Make the query tensor be column vectors so it can be used with a transposed dot product
x = torch.randn(3, 64)
