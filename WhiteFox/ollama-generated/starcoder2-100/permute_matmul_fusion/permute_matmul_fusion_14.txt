
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1  = x1.permute([0, 3, 1, 2])
        v2  = torch.bmm(v1, x2)
        return v2


# Initializing the model
m = Model()

 # Inputs to the model with different permutations of indices
x1_input = torch.randn([4,5])
x2_input = torch.randn([4,3, 28, 28])


 x2_out, 