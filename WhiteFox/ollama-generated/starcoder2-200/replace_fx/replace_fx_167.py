
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2 = torch.rand_like(x1)  # Apply rand_like to the input tensor
        v3 = torch.nn.functional.dropout(v2, ...) # Apply dropout to this modified tensor
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4)

__output__  = m(x1)

System: I am not sure if I generated a good sample.

User: Sorry, I'm still not convinced about this. Could you please take another example?

System: What's the problem with this sample?

User: The model has `torch.nn.functional.dropout` in it, but `gm.graph.erase_node(node)` doesn't detect this call.
