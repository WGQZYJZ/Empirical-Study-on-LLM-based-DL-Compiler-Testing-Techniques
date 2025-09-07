
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3 * 64, 8 * 12)
 
    def forward(self, x1):
        v1 = self.linear(x1).view(-1, 3, 8, 12)
        v2 = v1 - other_value() 
        return torch.relu(v2)


# Initializing the model and defining the 'other' value
m = Model()
other = 0

# Inputs to the model
x1  = torch.randn(3, 64, 8 * 12)
__output__  = m(x1)

# Saving the initial value of other_value() for re-loading later on
initial_value = torch.tanh(other())

# Changing 'other' to 0.5 so that the model will output the same result as it did with the initial value of 'other' set previously in m.forward()
other += 1 # Set other to 1 + 0.5 = 1.5, which is a valid output for the model and does not throw an error when calling m(x1) on the next line

