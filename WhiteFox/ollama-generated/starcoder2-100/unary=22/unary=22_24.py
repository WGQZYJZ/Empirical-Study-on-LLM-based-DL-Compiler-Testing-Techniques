class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0  = torch.nn.Linear(492658, 73)
        v1  = self.v0(x1) # Replace this line with your code here
        v2  = torch.tanh(v1)
 
        return v2
