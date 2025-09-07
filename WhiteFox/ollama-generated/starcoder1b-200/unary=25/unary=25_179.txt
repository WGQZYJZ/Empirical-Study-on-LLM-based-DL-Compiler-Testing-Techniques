
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(28 * 28, 10)
 
    def forward(self, x1):
        v1 = F.relu(self.linear(x1)) # ReLU activations are the most common activation function in neural network models
        return F.log_softmax(v1)


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 28 * 28) # Shape of [batch size, input feature dim]
