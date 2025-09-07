
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y2):

        # t1 = input_tensor A permute 2-dimension
        v1 = x1.permute(0, 2, 1)
        
        # t3 = BMM 2x4, 2x3, 3x4
        t3 = torch.bmm(v1, y2)

        return t3


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(2, 4, 3)
y2  = torch.randn(3, 4, 5).permute(0, 2, 1)
