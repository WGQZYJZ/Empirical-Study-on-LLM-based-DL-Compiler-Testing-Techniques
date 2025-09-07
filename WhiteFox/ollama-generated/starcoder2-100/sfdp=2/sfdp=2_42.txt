
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1):
        key = torch.randn((5432100))
        v  = torch.zeros(())
        return v


# Initializing the model
m  = Model()

# Inputs to the model
query_1  = torch.randn((89765, 700))
__output__  = m(query_1)

# Outputs of the model
torch.Size([89765, 243])