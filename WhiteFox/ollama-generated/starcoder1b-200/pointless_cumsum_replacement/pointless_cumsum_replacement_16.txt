
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dtype = torch.float64  # Set the dtype for generated inputs
        self.layout = "NCHW"     # Set the layout for generated inputs

    def forward(self, x1):
        v1 = x1  # Assign a copy of the input tensor to another variable
        t1 = torch.full([len(x1)], 1, dtype=self.dtype, device=None, pin_memory=False)
        t2 = convert_element_type(t1, self.dtype)
        t3 = torch.cumsum(t2, 1)
        return t3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn([2], 3, dtype=torch.float64, device=None, pin_memory=False)
