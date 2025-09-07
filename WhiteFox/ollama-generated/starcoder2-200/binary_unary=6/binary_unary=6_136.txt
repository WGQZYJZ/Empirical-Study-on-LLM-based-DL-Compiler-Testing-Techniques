
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 50, bias=True)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other # <other> should be a random value. It is not included in the following text because it may be used in more than one model. 
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(4, 128)
__output__  = m(x1)

# Saving inputs and outputs of a sample run in a file
f  = open("sample_run", "wb") # Sample_run will be used later for testing. You should name your file after the model you are testing.
torch.save({'x': x1, 'output': __output__}, f)
