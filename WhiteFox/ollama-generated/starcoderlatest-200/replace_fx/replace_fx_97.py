
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.nn.functional.dropout(x1, ...)  # Apply dropout to the input tensor
        v2 = torch.rand_like(x2)                    # Generate a tensor with the same size as input_tensor filled with random numbers
        return v1 * v2


# Initializing the model
m = Model()
torch._C._jit_set_graph_fuser_enabled(True)
gm.optimize_graph(m, inputs=[torch.randn(3, 4), torch.randn(3, 5)])

