
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2048, 1)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v3  = v1 + other_tensor
        v5  = v3.clamp(-max_val, max_val).relu()
        return v6


# Initializing the model
m  = Model()
 
 # Inputs to the model 
 x1  = torch.randn(2048)
 
 __output__  = m(x1)
 
 