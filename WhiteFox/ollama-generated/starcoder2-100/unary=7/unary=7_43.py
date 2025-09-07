
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(40,10)
 
    def forward(self, x1):
       v1  = self.linear(x1) + 3 #Apply the linear transformation to the input tensor with an additional bias value of `+3` 
       v2  = F.clamp(min=0., max=6.) * (v1 + 3) #Clamps the output from the previous linear transformation by 3 
       v4  = torch.div(v2, 6.).unsqueeze_(dim=-1)
        return v4

# Initializing the model