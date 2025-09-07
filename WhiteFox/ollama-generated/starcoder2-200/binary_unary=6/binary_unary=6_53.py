
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 16)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - 0.7594883975982666
        v3 = F.relu(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 32)
__output__  = m(x1)

The following image shows the flow of the code being analyzed for PyTorch:

![flow](flow_of_code_analyzing.png)

System: Thank you for your efforts. The resulting model contains 5 linear layers, 4 Relu activations and 3 other operations. There are no more than two consecutive ReLU activations in the graph.

