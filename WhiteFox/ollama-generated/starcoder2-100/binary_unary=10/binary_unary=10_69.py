
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(5120 + 5, 4)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other_tensor()
        v3 = relu_(v2) # Apply the ReLU activation function to the result
        return v3
# Initializing the model
m  = Model()

