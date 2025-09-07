
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32,10)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other  # where 'other' is a tensor of size (batch_size=32, output_dimension=10). 
        return v2


# Initializing the model and setting the value for keyword argument "other" to a fixed tensor.
other = torch.randn(32, 10) # 32 is batch size, 10 is number of classes in the dataset
m = Model()
m.linear.weight.data = other


# Inputs to the model and the keyword argument "other" for model initialization.
x1 = torch.randn(batch_size=32, input_dimension=32)
__output__  = m(x1)
