
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)
 
    def forward(self, x1):
        v1 = self.linear(x1) > 0 # Apply the Leaky ReLU function to t1 and store it in output_tensor2.
        negative_slope = -0.2
        v3 = v1 * negative_slope # Multiply the Leaky ReLU output by negative slope
        t4 = torch.where(v1, x1, v3) # For each element in t1, if the element is True, choose the corresponding element from input tensor x1, otherwise choose the corresponding element from output_tensor2
        return t4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 10)
