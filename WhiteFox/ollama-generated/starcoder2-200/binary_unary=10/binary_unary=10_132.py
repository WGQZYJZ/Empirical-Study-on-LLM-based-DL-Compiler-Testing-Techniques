
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3072, 10)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + other_tensor # You need to add another tensor here
        v3  = torch.relu(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
input_tensor=torch.randn(64, 3072)
other = torch.randn(64,10)# Add another tensor here # you need to add anoter tensor here

# Initialize the input for a different model with the same inputs as before
x2  = torch.randn_like(input_tensor)

__output__  = m(input_tensor), m(other_tensor), m(x1), m(x2)

