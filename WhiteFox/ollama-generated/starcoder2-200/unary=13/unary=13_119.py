
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 64)

    def forward(self, x1):
        v0 = F.linear(x1,  # Pass the input tensor to the linear transformation
            weight=torch.zeros([90]), bias=torch.zeros(1))
        v1 = F.sigmoid(v0)
        return torch.mul(v0, v1)


# Initializing the model and getting input_tensor:

m  = Model()
x1 = torch.randn(32).view(1,-1) # x is a batch of inputs for the model. 

__output__  = m(x1)