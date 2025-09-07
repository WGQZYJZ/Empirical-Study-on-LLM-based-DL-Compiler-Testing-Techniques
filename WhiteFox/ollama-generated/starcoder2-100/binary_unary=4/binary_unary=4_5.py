
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Linear(25, 8)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + other # Add another tensor to the output of the linear transformation
        
        v3  = torch.relu(v2)

        return v3

# Initializing the model
m  = Model()
other  = torch.randn(8, 25)

 # Inputs to the model
x1  = torch.randn(10, 25)

 # Generating the output tensor from the model. The output of the model should be different than that of previous examples. 
 __output__  = m(x1)

