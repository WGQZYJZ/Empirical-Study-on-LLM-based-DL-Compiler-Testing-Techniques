
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.cumsum = torch.cumsum
 
    def forward(self, x0, x1):
        v1  = torch.full([x0, x1], 1, dtype=torch.int32) 
        v2  = torch.int8(v1) 
        __output__  = self.cumsum(v2, 1)


# Initializing the model
m = Model()


# Inputs to the model
x0_input_size = torch.Size([5397]) # Shape of the input tensor x0
x1_input_size = int(-1 if not torch._C.get_python_uint32_overflown() else 0)  # Maximum size of the first dimension for the input tensors


# Initializing the model and generating the inputs to it
model, inputs = prepare_inputs([x0_input_size, x1_input_size])

