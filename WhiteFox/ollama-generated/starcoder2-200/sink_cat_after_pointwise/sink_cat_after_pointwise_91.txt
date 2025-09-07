
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v = torch.cat([x1, x2], 0) # Concatenate tensors along the batch dimension (dim=0)
        v = v.view(-1, 3) # Reshape the concatenated tensor after concatenation;
        v = torch.relu(v) # Apply ReLU to the reshaped tensor.
        return v

# Initializing the model
m = Model()


# Inputs to the model
t1  = torch.randn([2, 3])
t2  = torch.randn([3, 5])
__output__  = m(t1, t2)