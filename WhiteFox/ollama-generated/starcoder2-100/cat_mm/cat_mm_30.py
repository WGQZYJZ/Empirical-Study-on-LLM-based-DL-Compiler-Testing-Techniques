
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m = torch.nn.Embedding(2, 3)
 
    def forward(self, input1, input2):
        v1  = self.m(input1)
        v2  = torch.mm(v1, v1)
        v3  = torch.cat([v2 for i in range(len(input2))], dim=0)
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
input1  = torch.tensor([[i] for i in range(3)]) # This is a list containing three lists, each list contains one integer.
input2  = [torch.randn(size=(50))]*len(input1)
__output__  = m(*input1, input2)

