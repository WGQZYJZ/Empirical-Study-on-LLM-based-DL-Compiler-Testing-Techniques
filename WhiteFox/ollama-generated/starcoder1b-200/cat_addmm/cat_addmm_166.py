
class Model(torch.nn.Module):
    def __init__(self, num_inputs: int = 3):
        super().__init__()
        self.linear1 = torch.nn.Linear(num_inputs, 20)
 
    def forward(self, x1):
        # This is an example of concatenation along the last dimension with 2 dimensions as follows:
        # self.linear1(...) = <torch.nn.functional.linear>(x1, self.linear1(...)) + 2
        return self.linear1(...) + torch.randint(high=2, size=(1,), dtype=torch.int32)

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(5, 3)
y1 = m(x1)

