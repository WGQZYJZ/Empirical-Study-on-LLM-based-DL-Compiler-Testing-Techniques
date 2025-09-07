
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = input_tensor.permute(0, 2, 1).contiguous() # Permute the input tensor and make it contiguous, then add the `torch.nn.functional.dropout` function to the graph
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2

# Initializing the model
m = Model()

 # Input to the model
x1 = torch.randn(1, 2, 2)
