
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, ...) # Apply dropout to the input tensor
        v2 = torch.rand_like(v1, ...) # Generate a tensor with the same size as input_tensor filled with random numbers
        return v2


# Initializing the model and compiling the model
m = Model()
g_before_replace = m.generate_graph([torch.randn(1, 2, 2)], "fwd")
gm.replace_fx(gm.GraphModeEnum.FWD, g_before_replace)


# Initializing the model and compiling the model with the specified flags
m = Model()
g_with_flags = m.generate_graph([torch.randn(1, 2, 2)], "fwd", fallback_random=True)
gm.replace_fx(gm.GraphModeEnum.FWD, g_with_flags, gm.GraphModeFlag.FALLBACK_RANDOM)


# Inputs to the model
x1 = torch.randn(1, 2, 2)
