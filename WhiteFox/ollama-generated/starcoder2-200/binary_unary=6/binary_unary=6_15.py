
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 64)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other # 'other' is a constant
        v3 = F.relu(v2) # F refers to the module of pytorch
        return v3


# Initializing the model and setting 'other' as 5.0f
m  = Model()
other = 5.0


# Inputs to the model