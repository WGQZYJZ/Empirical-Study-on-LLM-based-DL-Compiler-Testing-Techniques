
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256*14*14, 3)
 
    def forward(self, x1):
        v1  = self.linear(x1) # Applying a linear transformation to the input tensor
        v2  = v1 + other  # Adding another constant Tensor
        v3  = torch.relu(v2)# Apply ReLU activation function to result
        return v3


# Initializing the model
m = Model()


# Inputs to the model
other = torch.randn(256*14*14, 3)
x1 = torch.randn(batch_size=1, channels=3, height=640, width=640)
 
__output__  = m(x1)

