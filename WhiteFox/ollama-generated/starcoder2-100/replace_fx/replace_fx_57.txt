
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = torch.nn.functional.dropout(x1, p=0.5) 
        # Apply dropout to the input tensor with probability of 0.5
        return v1

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(4)

