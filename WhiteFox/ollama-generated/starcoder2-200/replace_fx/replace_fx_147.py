
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 3)

    def forward(self, x1):
        v1  = torch.nn.functional.dropout(x1, 0.8, True)  # Apply dropout with p=0.8 to the input tensor 
        v2  = x1 + torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(100, 3, 5) + 5 

# Setting the input size and shape for each dim to 3. If we use more than one inputs in `torch.nn.functional.dropout` function, you need to set each dim separately.
m.input_size = (None, None, None) # Inferred from input tensor

