
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):

        y = torch.nn.functional.linear(x=x1)

        v6  = torch.nn.functional.relu(v5)
        return v6


# Initializing the model
m2 = Model()

# Inputs to the model
x1  = torch.randn(1,3,64,64)

# Input tensor that was used for training
x_tr = torch.randn(30958747,30958747).to('cuda')

# Model outputs with respect to the input tensors x1 and x2 using pytorch API 1
