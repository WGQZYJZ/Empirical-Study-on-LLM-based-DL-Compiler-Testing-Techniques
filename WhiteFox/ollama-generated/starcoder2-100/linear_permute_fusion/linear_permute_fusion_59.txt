
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)

    def forward(self, x):
        t1  = torch.nn.functional.linear(x, self.linear.weight, bias=None)
        return t1

# Initializing the model
m = Model()

 # Inputs to the model. The input tensor is randomly generated with 3 dimensions and contains a non-negative integer value.
x = torch.randn(28, 20, int(torch.rand(()).numpy()*5))

 # Output of the model on given inputs (m(x)). This output may also be another randomly generated tensor.
