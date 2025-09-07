
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(512, 1)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = torch.sigmoid(v1) 
        return v2


# Initializing the model
m = Model()

# Inputs to the model
input_tensor = torch.randn(320, 512)
output_vector = m(input_tensor).reshape(-1)
