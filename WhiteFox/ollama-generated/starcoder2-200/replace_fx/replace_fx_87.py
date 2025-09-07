
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1):
        t2 = torch.nn.functional.dropout(input1) # erase this line in the graph to trigger the `rand_like` replacement and erasing
        t3 = torch.rand_like(t2)  # erase this line of code to trigger a non-erasure
        return t3

m = Model()

# Input for the model
x1 = torch.randn(2, 4)

