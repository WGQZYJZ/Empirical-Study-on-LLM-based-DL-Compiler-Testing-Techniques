
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, t1, t2):
        v3 = torch.relu(t1 + t2) # ReLU is the only pointwise unary operation applied on the concatenated tensors.
        return v3

m  = Model()


# Inputs to the model
t1 = torch.randn([3])
t2 = torch.randn([4, 5])
__output__  = m(t1, t2)

