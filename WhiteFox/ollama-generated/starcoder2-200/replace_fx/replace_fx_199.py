
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 20) # Replace with dropout
        self.linear2 = torch.nn.Linear(35, 7) # Replace with rand_like

    def forward(self, x):
        t1 = torch.nn.functional.dropout(x, p=0.8) 
        t2 = torch.rand_like(t1).to(device=x.device) 
        return self.linear1(torch.cat((t1, t2), dim=-1)) + self.linear2(x)


# Initializing the model
m  = Model()

# Inputs to the model
x  = torch.randn(35).to(device="cpu") 

__output__  = m(x)