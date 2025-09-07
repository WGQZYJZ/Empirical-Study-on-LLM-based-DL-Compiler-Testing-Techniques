
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32768, 1)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.sigmoid(v1)
        v3  = v1 * v2
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(8, 64000).permute(1,0) # A 64 KB input to the model. This will trigger the gating mechanism in the code, as the output of the sigmoid function will control the flow of information.


