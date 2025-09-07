
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1): 
        t1 = torch.nn.functional.dropout(x1)
        t2 = torch.rand_like(t1) # This will be replaced by rand_like
        return torch.nn.functional.linear(t1, self.linear.weight, self.linear.bias)

# Initializing the model 
m  = Model()
x1 = torch.randn(2048*2048*3)
