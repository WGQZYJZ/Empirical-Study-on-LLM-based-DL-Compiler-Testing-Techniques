
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1  = x1 .permute(0, 2, 1)
        v2 = torch.bmm(v1, x2) 
        return v2


# Initializing the model
m = Model()

# Inputs to the model: two tensors for inputs and two corresponding target tensors for outputs; 
x1_input  = torch.randn(3072, 64, 89); x2_input  = torch.randn(3072, 53, 8)
x1_target = torch.randn(3072, 64, 89); x2_target = torch.randn(3072, 53, 8)
