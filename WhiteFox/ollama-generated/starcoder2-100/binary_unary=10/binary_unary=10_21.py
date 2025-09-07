
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32*32*8, 10)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + other_tensor
        v3  = F.relu(v2) # Apply the ReLU activation function to the result
        return v3

# Initializing the model
m = Model()


# Inputs to the model
input1, input2  = torch.randn(10000, 8), other_tensor=torch.randn(10000)


__output1__, __output2__  = m(input1), m(input2)
