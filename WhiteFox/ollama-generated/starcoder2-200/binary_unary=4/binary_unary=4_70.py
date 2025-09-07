
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3, 8)

    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + other # Add another tensor to the output of the linear transformation
        v3  = F.relu(v2) # Apply ReLU activation function to the result
        return v3


# Initializing and running the model
m  = Model()
m  = m.to('cuda')
other = torch.randn((1,8)).to('cuda')
x1   = torch.randn(1, 3).to('cuda')
__output__  = m(x1)

