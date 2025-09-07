
class Model(torch.nn.Module):
    def __init__(self, min_value=None, max_value=None):
        super().__init__()
        self.linear  = torch.nn.Linear(784, 20)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value) 
        return v3


# Initializing the model with input_tensor of shape (N, 784), where N is a positive integer, as input to the model's forward method and min value `min`, and max value `max`. Also provide `min` and `max` arguments.
m = Model(10, 32)


# Inputs to the model with shape (N, 784), where N is a positive integer, as input to the model's forward method
x1 = torch.randn(50, 784)
