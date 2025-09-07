
class Model(torch.nn.Module):
    def __init__(self, input1Size=2048, input2Size=3584, input3Size=60792, input4Size=2017):
        super().__init__()
 
        self.linear1 = torch.nn.Linear(input1Size, 512)
        self.linear2 = torch.nn.Linear(input2Size, 897)
        self.linear3 = torch.nn.Linear(input3Size, input4Size)
 
    def forward(self, x):
 
        v1 = self.linear1(x)
        v2 = self.linear2(v1)
        v3 = self.linear3(v2)
 
        return v3


# Initializing the model