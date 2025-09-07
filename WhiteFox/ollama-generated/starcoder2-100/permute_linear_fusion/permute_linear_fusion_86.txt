
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 1)

    def forward(self, x1):
        v1  = x1 .permute(0, 3, 1).reshape(x1.shape[...])  # Permute the input tensor and reshape it.
        v2  = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias) 
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(3 ,4,5)   # This is a 3d input tensor that contains 3 channels with size [batch_size=3], [height=4] and [width=5].
__output__  = m(x1)

