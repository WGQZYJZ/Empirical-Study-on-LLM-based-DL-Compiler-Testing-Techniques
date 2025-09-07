
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1, input2):
        v1  = torch.mm(input1, input2)
        return v1,


# Initializing the model and generating input tensors for it:

model  = Model()
input_1 = torch.randn(3072, 49658) + 4.9578
input_2 = torch.randn(3072, 49658) - 0.8208

