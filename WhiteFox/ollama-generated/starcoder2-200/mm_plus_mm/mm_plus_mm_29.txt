
class Model(torch.nn.Module):
    def __init__(self, input1 = torch.randn(32), input2  = torch.randn(32)):
        super().__init__()
        self.input1 = input1
        self.input2 = input2
 
    def forward(self, input1 = self.input1, input2 = self.input2):
        v1 = torch.mm(input1, input2) 
        v2  = torch.mm(input3, input4)
        v3 = v1 + v2  
        return v3

# Initializing the model with inputs