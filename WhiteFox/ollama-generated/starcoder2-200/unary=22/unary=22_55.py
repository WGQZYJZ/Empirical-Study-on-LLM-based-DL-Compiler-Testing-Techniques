
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(256, 10)
 
    def forward(self, x1):
        v1  = self.linear(x1) 
        v2  = torch.tanh(v1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(64, 512) 


# Running the code
out = m(x1)


# Please generate a valid PyTorch model example with public PyTorch APIs meets the specified requirements. Plus, please also generate the input tensor for the newly generated model.