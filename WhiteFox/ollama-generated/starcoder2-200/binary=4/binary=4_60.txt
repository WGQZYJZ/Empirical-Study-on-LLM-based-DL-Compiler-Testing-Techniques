
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3072,1)
 
    def forward(self, x):
        v  = self.linear(x)
        return v + torch.randn_like(v)*5

# Initializing the model
model2  = Model2()

