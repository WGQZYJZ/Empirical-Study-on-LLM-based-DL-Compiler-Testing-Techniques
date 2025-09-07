
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.tanh(v1) # The hyperbolic tangent function is applied to the output of the linear transformation
        return v2


# Initializing and evaluating the model
m  = Model()
x1 = torch.randn(64, 784)
y_true = torch.ones(64, 10)
 
__output__  = m(x1) # Predicting the class probabilities using forward pass

