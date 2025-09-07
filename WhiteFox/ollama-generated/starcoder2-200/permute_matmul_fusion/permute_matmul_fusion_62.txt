
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y1):  # y is also a model input
        v2 = torch.bmm(x1.permute(0, 2, 1), y1) 
        return v2


# Initializing the model and inputs to it
m = Model()
input_tensor_A = torch.randn(3, 4, 5)
input_tensor_B = torch.randn(3, 5, 6)
