
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input):
        mat1 = torch.randn([240, 8])
        mat2 = torch.randn([8, 360])
 
        v1 = torch.addmm(input, mat1, mat2)

        v2 = torch.cat([v1], dim=2)

        return v2


# Initializing the model
m  = Model()

# Inputs to the model